
import inspect

from typing import Callable
from appams.services import messagebus, use_case_handler, use_case_unit_of_work
from appams.proxies import redis_publisher


def bootstrap(
    uow: use_case_unit_of_work.AbstractUnitOfWork = use_case_unit_of_work.UseCaseUnitOfWork(),
    publish_redis: Callable = redis_publisher.publish_message
) -> messagebus.MessageBus:

    # Podemos definir tantas dependencias como queramos: clases, referencias a funciones,...las cuáles son parámetros
    # en las funciones handler.
    dependencies = {'unit_of_work': uow, 'publish': publish_redis}

    # Forma base.
    # injected_event_handler = use_case_handler.EVENT_HANDLERS
    # injected_command_handler = use_case_handler.COMMAND_HANDLERS

    injected_event_handler = {
        event_type: [
            inject_dependencies(handler, dependencies) for handler in event_handlers
        ] for event_type, event_handlers in use_case_handler.EVENT_HANDLERS.items()
    }

    injected_command_handler = {
        command_type: inject_dependencies(handler, dependencies) for command_type, handler in use_case_handler.COMMAND_HANDLERS.items()
    }

    return messagebus.MessageBus(
        uow=uow,
        event_handler=injected_event_handler,
        command_handler=injected_command_handler
    )


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }

    return lambda message: handler(message, **deps)
