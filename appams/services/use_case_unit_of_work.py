
import abc
import logging

from appams.repository import use_case_repository
from appams.domain import entity_model

logging.basicConfig(level=logging.DEBUG)


class AbstractUnitOfWork(abc.ABC):

    repository: use_case_repository.AbstractUseCaseRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError

    @abc.abstractmethod
    def view_use_case(self):
        """
        Returns the data from the database.
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_elem_to_database(self, elem: entity_model.BaseEntity):
        raise NotImplementedError

    def collect_new_events(self):
        """
        Get processed entities.

        :return: Set[entity_model.UseCaseEntity]

        """
        if len(self.repository.procesed) > 0:
            for entity in self.repository.procesed:
                while entity.events:
                    yield entity.events.pop(0)


class UseCaseUnitOfWork(AbstractUnitOfWork):

    """Database define the reference to database simulate"""
    # database: [entity_model.UseCaseEntity]

    def __init__(self):
        self.repository = use_case_repository.UseCaseRepository()
        self.repository.init_database([
            entity_model.UseCaseEntity(uuid="{12345678-1234-5678-1234-567812345678}",
                                       name="Name1",
                                       operation="+",
                                       operator=10),
            entity_model.UseCaseEntity(uuid="{12345678-1234-5678-1234-567812345699}",
                                       name="Name2",
                                       operation="+",
                                       operator=20)
        ])

    def __enter__(self):
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def __exit__(self, *args):
        super().__exit__(*args)

    def commit(self):
        logging.info(f'Commit done')

    def rollback(self):
        logging.info(f'Rollback done....')

    def view_use_case(self):
        return self.repository.load_database()

    def add_elem_to_database(self, elem: entity_model.BaseEntity):
        self.repository.load_database().append(elem)
