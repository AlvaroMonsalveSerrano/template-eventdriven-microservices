from appams.domain import events
from appams.services import use_case_handler, use_case_unit_of_work


def test_publish_message_redis():
    event_test = events.SendEvent(to="a@a.es", subject="test", operation="+")

    resultado = use_case_handler.publish_message_to_redis(
        event=event_test,
        unit_of_work=use_case_unit_of_work.UseCaseUnitOfWork())

    assert resultado == 1
