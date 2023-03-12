from enum import Enum


class ElementType(Enum):
    REST = 0
    NOTE = 1


class ScoreElement:
    def __init__(self, element_type: ElementType, length, pitch):
        self._type = element_type  # Note or rest
        self._length = length  # Length of the note in 16ths
        self._pitch = pitch  # Pitch name for notes, r for rests

    def get_type(self):
        return self._type

    def get_length(self):
        return self._length

    def get_pitch(self):
        return self._pitch
