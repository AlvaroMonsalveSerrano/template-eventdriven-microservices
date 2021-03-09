
import redis
import logging
import json
from appams import config
from appams.exceptions import redis_exception

logging.basicConfig(level=logging.DEBUG)


def start(redis_server: redis.Redis) -> None:
    """
    Get a message from Redis topic.

    :param redis_server: redis.Redis
    :return: None
    """
    logging.info(f"[##] Consuming message...")

    if redis_server is None:
        raise redis_exception.ConsumerRedisException()

    consume_client_topic = redis_server.pubsub()
    consume_client_topic.subscribe(config.TOPIC_REDIS)

    for message in consume_client_topic.listen():
        if message['data'] != 1:
            data = json.loads(message['data'].decode())
            logging.info(f"mesagge={data['message']} result={data['result']}")


def main():
    """
    Main function.

    :return: None
    """
    logging.info(f"## Consumer ##")
    redis_server = redis.Redis(**config.get_redis_configuration())
    logging.info(f"[##] Redis connected")
    start(redis_server)


if __name__ == '__main__':
    main()
