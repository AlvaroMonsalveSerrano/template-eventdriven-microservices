import abc
import uuid
import logging

from typing import Set

from appams.domain import entity_model

logging.basicConfig(level=logging.DEBUG)


class AbstractUseCaseRepository(abc.ABC):
    """
    Abstract class with the common operations of the entity UseCaseEntity
    """

    procesed: Set[entity_model.UseCaseEntity]

    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def add(self, entity: entity_model.UseCaseEntity) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uuid: str) -> entity_model.UseCaseEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def init_database(self, data_list: [entity_model.UseCaseEntity]):
        raise NotImplementedError

    @abc.abstractmethod
    def load_database(self) -> [entity_model.UseCaseEntity]:
        raise NotImplementedError


class UseCaseRepository(AbstractUseCaseRepository):
    """
    Definition of the operations that connect to database.
    """

    def __init__(self) -> None:
        self.database: [entity_model.UseCaseEntity] = []
        self.procesed = set()  # type: Set[entity_model.UseCaseEntity]

    def init_database(self, data_list: [entity_model.UseCaseEntity]):
        if data_list is not None:
            self.database = data_list

    def load_database(self) -> [entity_model.UseCaseEntity]:
        return self.database

    def add(self, entity: entity_model.UseCaseEntity) -> bool:
        result: bool = False
        logging.info(f"[***] /use_case_repository.add")
        if entity is not None:
            result = True
            self.database.append(entity)
            self.procesed.add(entity)
        return result

    def get(self, p_uuid: str) -> entity_model.UseCaseEntity:
        index = 0
        enc = False
        result: entity_model.UseCaseEntity = None
        logging.info(f"[***] /use_case_repository.get")
        while (index < len(self.database)) and not enc:
            aux: entity_model.UseCaseEntity = self.database[index]
            if aux.uuid == uuid.UUID(p_uuid):
                result = aux
                self.procesed.add(result)
                enc = True
            index += 1
        return result
