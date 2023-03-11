from enum import Enum


class ElementType(Enum):
    REST = 0
    NOTE = 1


class ScoreElement:
    def __init__(self, element_type: ElementType, length, pitch=None):
        self._type = element_type
        self._length = length
        self._pitch = pitch
