from dataclasses import dataclass

from api.application.domain.event_types import EventType

from .queries_dto_interface import QueryDtoInterface


@dataclass
class QueriesDTO(QueryDtoInterface):

    obj1: object
    obj2: object
    id: str
    event: EventType

    def all_records(self, obj1):
        return obj1.all()

    def one_record(self):
        return super().one_record()

    def existence(self, obj1):
        return obj1.exist()

    def update_record(self):
        return super().update_record()

    def create_record(self):
        return super().create_record()