
import json
import logging

from appams.services import use_case_unit_of_work

logger = logging.getLogger(__name__)


def view_use_case(uuid: str, unit_of_work: use_case_unit_of_work.AbstractUnitOfWork):
    with unit_of_work:
        result = unit_of_work.view_use_case()
        logger.info(f'Result={result}')
        return json.dumps([register.__dict__ for register in result])

