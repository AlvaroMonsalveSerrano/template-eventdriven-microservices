
import logging

from dataclasses import asdict
from appams import config
from appams.domain import entity_model, events, commands
from appams.exceptions import use_case_exception
from appams.proxies import redis_publisher
from . import use_case_handler, api_service, use_case_unit_of_work, email_service


def do_something(message: commands.CommandAction1UseCase,
                 unit_of_work: use_case_unit_of_work.AbstractUnitOfWork) -> entity_model.UseCaseResponse:
    """
    Business operation.

    :param message: entity_model.UseCaseRequest
    :param repository: use_case_repository.AbstractUseCaseRepository
    :param unit_of_work: use_case_unit_of_work.AbstractUnitOfWork

    :return: entity_model.UseCaseResponse
    """

    if message is None or unit_of_work is None:
        raise use_case_exception.UseCaseRequestException()

    logging.info(f"[**] /use_case_service.do_something")

    entity = entity_model.UseCaseEntity(uuid=str(message.uuid),
                                        name=message.name,
                                        operation=message.operation,
                                        operator=message.operator,
                                        date_data=None)  # date.today()

    with unit_of_work:
        result = entity_model.UseCaseResponse(str(entity.calculate))
        unit_of_work.repository.add(entity)
        unit_of_work.commit()

    return result


def add_entity_to_read_model_view(
        event: events.AddUseCaseEntity,
        unit_of_work: use_case_unit_of_work.AbstractUnitOfWork) -> entity_model.UseCaseResponse:
    logging.info(f"[**] /add_entity_to_read_model_view; event={asdict(event)}")
    unit_of_work.add_elem_to_database(
        entity_model.UseCaseEntity(uuid=event.uuid,
                                   name=event.name,
                                   operation=event.operation,
                                   operator=event.operator)
    )


def send_email(event: events.SendEvent,
               unit_of_work: use_case_unit_of_work.AbstractUnitOfWork) -> bool:
    """
    Mail delivery service

    :param event: events.SendEvent
    :param unit_of_work: use_case_unit_of_work.AbstractUnitOfWork
    :return: entity_model.SendMailResponse
    """
    logging.info(f"[**] /use_case_service.send_email; "
                 f"to={event.to}, "
                 f"subject={event.subject}, "
                 f"operation={event.operation}")
    return email_service.send_mail(event.to, event.subject, event.operation)


def publish_message_to_redis(event: events.SendEvent,
                             unit_of_work: use_case_unit_of_work.AbstractUnitOfWork):
    logging.info(f"[**] /use_case_service.publish_message_to_redis; "
                 f"to={event.to}, "
                 f"subject={event.subject}, "
                 f"operation={event.operation}")

    return redis_publisher.publish_message(config.TOPIC_REDIS, event)


EVENT_HANDLERS = {
    # TODO No se usa este evento. Analizar para eliminarlo. Ver si tiene sentido.
    events.AddUseCaseEntity: [
        add_entity_to_read_model_view
    ],
    events.SendEvent: [
        send_email,
        publish_message_to_redis
    ]

}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.Liveness: api_service.do_liveness,
    commands.Rediness: api_service.do_rediness,
    commands.CommandAction1UseCase: do_something

}  # type: Dict[Type[commands.Command], Callable]