from appams.domain import commands

from appams import bootstrap
from appams.services import messagebus

from . import test_use_case_service


def bootstrap_test() -> messagebus.MessageBus:
    """
    Create Test MessageBus.
    """
    return bootstrap.bootstrap(uow=test_use_case_service.FakeUseCaseUnitOfWork())


def test_do_liveness():

    command = commands.Liveness()

    bus = bootstrap_test()
    result: [str] = bus.handle(message=command)

    assert result is not None
    assert len(result) == 1
    assert result[0] == "Ok"


def test_do_rediness():

    command = commands.Rediness()

    bus = bootstrap_test()
    result: [str] = bus.handle(message=command)

    assert result is not None
    assert len(result) == 1
    assert result[0] == "Ok"
