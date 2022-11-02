from abc import ABC, abstractmethod
from django.db import DatabaseError

class QueryDtoInterface(ABC):

    @abstractmethod
    def all_records(self):
        raise DatabaseError

    @abstractmethod
    def one_record(self):
        raise DatabaseError

    @abstractmethod
    def existence(self):
        raise DatabaseError