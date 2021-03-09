
import logging

from typing import List, Dict, Callable, Type, Union
from appams.domain import events, commands
from appams.exceptions import message_bus_exception
from . import use_case_unit_of_work

logger = logging.getLogger(__name__)

Message = Union[commands.Command, events.Event]


class MessageBus:

    def __init__(self,
                 uow: use_case_unit_of_work.AbstractUnitOfWork,
                 event_handler: Dict[Type[events.Event], List[Callable]],
                 command_handler: Dict[Type[commands.Command], Callable]):
        self.uow = uow
        self.event_handlers = event_handler
        self.command_handlers = command_handler
        self.queue = []

    def handle(self, message: Message):
        results = []
        self.queue = [message]
        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, events.Event):
                self.handle_event(message)

            elif isinstance(message, commands.Command):
                result_command = self.handle_command(message)
                results.append(result_command)

            else:
                raise message_bus_exception.ProcessMessageBusException(f"Error process message: {message} error")

        return results

    def handle_event(
            self,
            event: events.Event):

        for handler in self.event_handlers[type(event)]:
            try:
                logger.debug(f"Event: {event}. Handler: {handler}")
                handler(event)
                self.queue.extend(self.uow.collect_new_events())

            except Exception as ex:
                logger.exception(f"Exception handling event {event}. Exception: {ex}")
                continue

    def handle_command(
            self,
            command: events.Event):
        """
        El command no retorna nada porque en la vista se ve el resultado. Patrón CQS?
        :param command:
        :return:
        """

        try:
            logger.debug(f"Command: {command}")
            handler = self.command_handlers[type(command)]
            result = handler(command)  # unit_of_work=self.uow
            self.queue.extend(self.uow.collect_new_events())

        except Exception as ex:
            logger.exception(f"Exception handling command {command}. Exception: {ex}")
            raise ex

        return result





