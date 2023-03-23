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
        # self._score = ""
        self._path = os.path.join(self._dodec.foldername, self._dodec.filename)

        # The number of 16th notes per measure
        self._value_per_measure = self._dodec.time_enumerator * (16 / self._dodec.time_denominator)

        # The lengths of the different element types, ordered from longest to shortest - counted in 16ths.
        self._lengths_py = [16, 24, 8, 12, 4, 6, 2, 3, 1, 16, 24, 8, 12, 4, 6, 2, 3, 1]
        # Helper list for the random function to select an element from the available elements.
        self._range = range(18)

        # The chances for notes and rests must be calculated from their relative chances within their element type
        # (notes or rests) and the chance for note vs rest.
        self._chances = [self._dodec.notes_value * x for x in self._dodec.note_chances.values()] + \
                        [self._dodec.rests_value * y for y in self._dodec.rest_chances.values()]

        # The dodecaphony score as expressed in a list of voices that each consist of score_elements, plus metadata
        # for each object level.
        self.Composition = score.Score()

    def generate_repeat(self, series):
        """Create one repeat of the series for one of the voices and return it."""
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
                pitch = 'r'
            length = self._lengths_py[next_type[0]]
            series_repeat.append(score_element.ScoreElement(element_type, length, pitch))

            current_note = series_repeat[-1]
            if len(series_repeat) > 1:
                repeat_previous_possible = True
                previous_note = series_repeat[-2]
            else:
                repeat_previous_possible = False
            # Look at the current note chance and add extra note(s) based on that.
            if element_type.NOTE:
                try_again = True
                while try_again:
                    if repeat_previous_possible:
                        repeat_previous_note = random.randint(0, 100)
                        if repeat_previous_note <= self._dodec.previous_chance:
                            # If you repeat the previous note, you should also repeat the current note after that.
                            series_repeat.append(previous_note)
                            series_repeat.append(current_note)
                    repeat_current_note = random.randint(0, 100)
                    if repeat_current_note <= self._dodec.current_chance:
                        series_repeat.append(current_note)
                    else:
                        try_again = False
        return series_repeat

    def generate_composition(self):
        """Generate each voice separately, one repeat at a time."""
        for voice in self._dodec.voices:
            new_voice = self.Composition.add_voice(voice)
            for i in range(self._dodec.repeats):
                # Generate the repeat based on the series and the provided characteristics
                # First, determine the variation of this repeat
                variation = random.randint(0, 3)
                if variation == Variations.SERIES.value:
                    new_voice.add(self.generate_repeat(self._dodec.series))
                elif variation == Variations.INVERSE.value:
                    new_voice.add(self.generate_repeat(self._dodec.inverse))
                elif variation == Variations.RETROGRADE.value:
                    new_voice.add(self.generate_repeat(self._dodec.retrograde))
                else:  # RETROGRADEINVERSE
                    new_voice.add(self.generate_repeat(self._dodec.retrograde_inverse))

    def generate_series_preview(self):
        for voice in self._dodec.voices:
            new_voice = self.Composition.add_voice(voice)
            series = []
            for note in self._dodec.series:
                pitch = note
                element_type = ElementType.NOTE
                length = 16
                series.append(score_element.ScoreElement(element_type, length, pitch))
            new_voice.add(series)
