
import redis
import logging

from dataclasses import asdict
from appams import config
from appams.domain import events

logger = logging.getLogger(__name__)

redis_server = redis.Redis(**config.get_redis_configuration())


def publish_message(topic_channel: str, message: events.Event) -> int:
    """
    Publish a message in Redis

    :param topic_channel: str
    :param message: events.Event

    :return: None
    """
    logger.debug(f"[***] Publishing: topic={topic_channel}, message={message}")
    msg = '{"message": "Send mail to: %s", "result": "OK"}' % asdict(message)
    return redis_server.publish(topic_channel, msg)


