
import uuid
from dataclasses import dataclass
from appams.domain import events


class Command:
    pass


@dataclass()
class CommandAction1UseCase(Command):
    """
    Command for action1 to case use do_something.

    """
    uuid: uuid.UUID
    name: str
    operation: str
    operator: int


@dataclass
class Rediness(Command):
    """
    Event to rediness endpoint.

    """
    pass


@dataclass
class Liveness(Command):
    """
    Event to Liveness endpoint.

    """
    pass
