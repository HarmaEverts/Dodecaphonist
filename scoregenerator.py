import os
import random
import dodecaphony
import score
import score_element
from score_element import ElementType
from enum import Enum


class Variations(Enum):
    SERIES = 0
    INVERSE = 1
    RETROGRADE = 2
    RETROGRADEINVERSE = 3


class ScoreGenerator:
    def __init__(self, dodec: dodecaphony.Dodecaphony):
        self._dodec = dodec
        self._score = ""
        self._path = os.path.join(self._dodec.foldername, self._dodec.filename)
        self._value_per_measure = self._dodec.time_enumerator * (16 / self._dodec.time_denominator)
        self._lengths_ly = ["1", "1.", "2", "2.", "4", "4.", "8", "8.", "16", "1", "1.", "2", "2.", "4", "4.", "8",
                            "8.",
                            "16"]  # Ordered from longest to shortest - counted in 16ths
        self._lengths_py = [16, 24, 8, 12, 4, 6, 2, 3, 1, 16, 24, 8, 12, 4, 6, 2, 3, 1]
        self._range = range(18)
        self._chances = list(self._dodec.note_chances.values()) + list(
            self._dodec.rest_chances.values())  # Same order as lengths
        self.Composition = score.Score()

    def generate_repeat(self, series):
        series_repeat = []
        counter = 0
        # Keep adding notes/rests until one series is complete.
        # Keep track of the note range to make sure that the line stays within the boundaries.
        # Decide whether to add a note or a rest
        while counter < 12:
            next_type = random.choices(self._range, self._chances)
            if next_type[0] < 9:  # Note
                pitch = series[counter]
                element_type = ElementType.NOTE
                counter += 1
            else:  # Rest
                element_type = ElementType.REST
            length = self._lengths_ly[next_type[0]]
        return score_element.ScoreElement(element_type, length, pitch)

    def generate_composition(self):
        # For each voice, generate the number of repeats for the series.
        for voice in self._dodec.voices:
            new_voice = self.Composition.add_voice(voice)
            for i in range(self._dodec.repeats):
                # Generate the repeat based on the series and the provided characteristics
                # First, determine the variation of this repeat
                variation = random.randint(0, 3)
                if variation == Variations.SERIES:
                    new_voice.add_repeat(self.generate_repeat(self._dodec.series))
                elif variation == Variations.INVERSE:
                    new_voice.add_repeat(self.generate_repeat(self._dodec.inverse))
                elif variation == Variations.RETROGRADE:
                    new_voice.add_repeat(self.generate_repeat(self._dodec.retrograde))
                else:  # RETROGRADEINVERSE
                    new_voice.add_repeat(self.generate_repeat(self._dodec.retrograde_inverse))

