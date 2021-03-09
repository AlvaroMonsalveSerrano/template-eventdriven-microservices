from dataclasses import dataclass
from datetime import date
from typing import Optional

from . import events


# TODO  A eliminar. Semánticamente no tiene sentido porque trabajamos con eventos.
@dataclass(unsafe_hash=True)
class UseCaseRequest:
    uuid: str
    name: str
    operation: str
    operator: int


@dataclass(unsafe_hash=True)
class UseCaseResponse:
    resul: str


class BaseEntity:
    pass


class UseCaseEntity(BaseEntity):

    def __init__(self,
                 uuid: str,
                 name: str,
                 operation: str,
                 operator: int,
                 date_data: Optional[date] = None):
        self.uuid = uuid
        self.name = name
        self.operation = operation
        self.operator = operator
        self.date = date_data
        self.events = []  # type: List[events.Event]

    @property
    def calculate(self) -> int:
        if self.operation == "+":
            result = self.operator + self.operator
            # self.events.append(
            #     events.AddUseCaseEntity(
            #         uuid=self.uuid,
            #         name=self.name,
            #         operation=self.operation,
            #         operator=self.operator)
            # )
        elif self.operation == "*":
            result = self.operator * self.operator
            # self.events.append(
            #     events.AddUseCaseEntity(
            #         uuid=self.uuid,
            #         name=self.name,
            #         operation=self.operation,
            #         operator=self.operator)
            # )
        else:
            self.events.append(
                events.SendEvent(
                    to="name@domain.es",
                    subject="Operation not valid",
                    operation=self.operation)
            )
            result = -1
        return result


@dataclass(unsafe_hash=True)
class SendMailResponse:
    resul: str