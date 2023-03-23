import score_element
from enum import Enum


class VoiceTypes(Enum):
    SOPRANO = 1
    MEZZOSOPRANO = 2
    ALTO = 3
    TENOR = 4
    BARITONE = 5
    BASS = 6


class Voice:
    def __init__(self, voice_type: VoiceTypes):
        self._voice_type = voice_type
        self._melody = []

    def get_voice_type(self):
        return self._voice_type

    def get_melody(self):
        return self._melody

    def add(self, repeat):
        self._melody += repeat
