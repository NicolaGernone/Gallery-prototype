from dataclasses import dataclass
from .queries_dto_interface import QueryDtoInterface

@dataclass
class QueriesDTO(QueryDtoInterface):

    obj1: object
    obj2: object

    def all_records(self, obj1):
        return obj1.all()

    def one_record(self):
        return super().one_record()

    def existence(self):
        return super().existence()