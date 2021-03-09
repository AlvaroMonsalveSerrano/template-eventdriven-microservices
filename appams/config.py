import os

# HOST_REDIS = "redis"
HOST_REDIS = "172.17.0.2"
PORT_REDIS = 6379
TOPIC_REDIS = "topic_poc"


def get_api_url():
    """
    Create url.

    :return: Str, http://{host}:{port}
    """
    host = os.environ.get('API_HOST', 'localhost')
    port = 5000 if host == 'localhost' else 80
    return f"http://{host}:{port}"


def get_redis_configuration():
    """
    Load Redis configuration.

    :return: dict with redis configuration.
    """

    env = os.environ.get("ENV", "local")

    if env == 'local':
        host = os.environ.get("REDIS_HOST", "172.17.0.2")
    else:
        host = 'redis'

    port = 6379
    return dict(host=host, port=port, db=0)
