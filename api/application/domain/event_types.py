from enum import Enum


class EventType(Enum):
    """ Type of events allowed on an image"""

    view = 'view'
    click = 'click'
