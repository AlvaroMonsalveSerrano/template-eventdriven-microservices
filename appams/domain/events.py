
import uuid

from dataclasses import dataclass


class Message:
    pass


class Event:
    pass


@dataclass
class AddUseCaseEntity(Event):
    """
    Event to case use do_something.

    """
    uuid: uuid.UUID
    name: str
    operation: str
    operator: int


@dataclass()
class SendEvent(Event):
    to: str
    subject: str
    operation: str
