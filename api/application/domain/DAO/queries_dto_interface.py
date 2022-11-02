from abc import ABC, abstractmethod
from django.db import DatabaseError

class QueryDtoInterface(ABC):

    @abstractmethod
    def all_records():
        raise DatabaseError