
import uuid
import pytest
import logging

from unittest.mock import patch

from appams.domain import entity_model, events, commands
from appams.services import use_case_handler, use_case_unit_of_work
from appams.exceptions import use_case_exception
from appams.repository import use_case_repository


class FakeUseCaseRepository(use_case_repository.AbstractUseCaseRepository):
    """
    FakeUseCaseRepository to test.

    """

    def __init__(self) -> None:
        super().__init__()

    def add(self, entity: entity_model.UseCaseEntity) -> bool:
        return True

    def get(self, uuid: str) -> entity_model.UseCaseEntity:
        return entity_model.UseCaseEntity(
                        uuid=uuid.UUID('{12345678-1234-5678-1234-567812345678}'),
                        name="name",
                        operation="+",
                        operator=10,
                        date_data=None)

    def init_database(self, data_list: [entity_model.UseCaseEntity]):
        list()

    def load_database(self) -> [entity_model.UseCaseEntity]:
        list()


class FakeUseCaseUnitOfWork(use_case_unit_of_work.AbstractUnitOfWork):

    def __init__(self):
        self.procesed = set()  # type: Set[entity_model.UseCaseEntity]

    def __enter__(self):
        self.repository = FakeUseCaseRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def __exit__(self, *args):
        super().__exit__(*args)

    def commit(self):
        logging.info(f'Commit done')

    def rollback(self):
        logging.info(f'Rollback done....')

    def collect_new_events(self):
        return set()

    def view_use_case(self):
        return list()

    def add_elem_to_database(self, elem: entity_model.BaseEntity):
        return list()


def test_do_something():
    uuid_test = uuid.UUID('{12345678-1234-5678-1234-567812345678}')

    command = commands.CommandAction1UseCase(uuid=uuid_test,
                                             name="name",
                                             operation="+",
                                             operator=10)

    result = use_case_handler.do_something(message=command, unit_of_work=FakeUseCaseUnitOfWork())
    assert result.resul == '20'


def test_do_something_request_is_none():
    with pytest.raises(use_case_exception.UseCaseRequestException):
        use_case_handler.do_something(None, FakeUseCaseUnitOfWork())


def test_send_email():
    event_test = events.SendEvent(to="a@a.es", subject="test", operation="+")
    result = use_case_handler.send_email(event=event_test, unit_of_work=FakeUseCaseUnitOfWork())
    assert result is not None
    assert result is True


@patch("appams.proxies.redis_publisher.publish_message")
def test_publish_message(mock_redis_publisher):
    event_test = events.SendEvent(to="a@a.es", subject="test", operation="+")

    mock_redis_publisher.return_value = 1
    resultado = use_case_handler.publish_message_to_redis(event=event_test, unit_of_work=FakeUseCaseUnitOfWork())

    assert mock_redis_publisher.called==True
    assert resultado == 1
