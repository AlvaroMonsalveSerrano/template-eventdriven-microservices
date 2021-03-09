
import logging
import redis

from appams import config
from appams.domain import commands
from appams.services import use_case_unit_of_work


def do_liveness(command: commands.Liveness,
                unit_of_work: use_case_unit_of_work.AbstractUnitOfWork) -> str:
    logging.info(f"[**] /api_service.do_liveness")
    return 'Ok'


def do_rediness(command: commands.Rediness,
                unit_of_work: use_case_unit_of_work.AbstractUnitOfWork) -> str:
    logging.info(f"[**] /api_service.do_rediness")

    result = 'Ok'
    try:
        redis_server = redis.Redis(**config.get_redis_configuration())
        redis_server.ping()

    except Exception as ex:
        result = 'Ko'
        logging.error(f"[**] /api_service.do_rediness. Exception: {str(ex)}")
    else:
        redis_server.close()

    return result
