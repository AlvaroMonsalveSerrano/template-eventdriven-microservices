
import uuid

from unittest import mock
from appams.domain import events, entity_model, commands

from appams.services import messagebus

from appams import bootstrap

from . import test_use_case_service


def bootstrap_test() -> messagebus.MessageBus:
    """
    Create Test MessageBus.
    """
    return bootstrap.bootstrap(uow=test_use_case_service.FakeUseCaseUnitOfWork())


def test_command_handler():
    uuid_test = uuid.UUID('{12345678-1234-5678-1234-567812345678}')

    command = commands.CommandAction1UseCase(uuid=uuid_test,
                                             name="name",
                                             operation="+",
                                             operator=10)

    bus = bootstrap_test()
    result: [entity_model.UseCaseResponse] = bus.handle(message=command)

    assert result is not None
    assert len(result) == 1
    assert result[0].resul == str(20)


def test_event_send_email():

    event = events.SendEvent(to="a@servermail.es",
                             subject="Subject",
                             operation="+")

    bus = bootstrap_test()
    with mock.patch("appams.services.email_service.send_mail") as mock_send_mail:
        bus.handle(message=event)
        assert mock_send_mail.call_args == mock.call("a@servermail.es", "Subject", "+")


