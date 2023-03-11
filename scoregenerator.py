import os
import random
import dodecaphony
from enum import Enum


class Variations(Enum):
    SERIES = 0
    INVERSE = 1
    RETROGRADE = 2
    RETROGRADEINVERSE = 3


class VoiceTypes(Enum):
    SOPRANO = 1
    MEZZOSOPRANO = 2
    ALTO = 3
    TENOR = 4
    BARITONE = 5
    BASS = 6


class ScoreGenerator:
    def __init__(self, dodec: dodecaphony.Dodecaphony):
        self._dodec = dodec
        self._composition = ""
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

    def generate_repeat(self, series):
        series_repeat = ""
        counter = 0
        # Keep adding notes/rests until one series is complete.
        # Keep track of the note range to make sure that the line stays within the boundaries.
        # Decide whether to add a note or a rest
        while counter < 12:
            next_type = random.choices(self._range, self._chances)
            if next_type[0] < 9:  # Note
                series_repeat += series[counter]
                counter += 1
            else:  # Rest
                series_repeat += "r"
            series_repeat += self._lengths_ly[next_type[0]]
            series_repeat += " "
        series_repeat += "\n"
        return series_repeat

    def create_voice_preamble(self, voice):
        preamble = ""
        if voice in range(1, 4):  # G clef
            preamble += "\n\\new Staff = \""
            if voice == 1:
                preamble += "Soprano\" "
                preamble += "<<\n\\new Voice = \"vocal\" \\with {\n\\remove \"Forbid_line_break_engraver\"\n}\n"
                preamble += "{ \\fixed g' { \n\\tempo 4 = "
            elif voice == 2:
                preamble += "Mezzo-soprano\" "
                preamble += "<<\n\\new Voice = \"vocal\" \\with {\n\\remove \"Forbid_line_break_engraver\"\n}\n"
                preamble += "{ \\fixed e' { \n\\tempo 4 = "
            elif voice == 3:
                preamble += "Alto\" "
                preamble += "<<\n\\new Voice = \"vocal\" \\with {\n\\remove \"Forbid_line_break_engraver\"\n}\n"
                preamble += "{ \\fixed c' { \n\\tempo 4 = "
            tempo = str(self._dodec.tempo)
            preamble += tempo
            preamble += "\n\\set midiInstrument = #\"flute\"\n\\clef \"treble\" \n\\key c \\major\n\\time "
            preamble += str(self._dodec.time_enumerator)
            preamble += "/"
            preamble += str(self._dodec.time_denominator)
            preamble += "\n"
        elif voice == 4:  # G clef octave down
            preamble += "\n\\new Staff = \"Tenor\""
            preamble += "<<\n\\new Voice = \"vocal\" \\with {\n\\remove \"Forbid_line_break_engraver\"\n}\n"
            preamble += "{ \\fixed g { \n\\tempo 4 = "
            preamble += str(self._dodec.tempo)
            preamble += "\n\\set midiInstrument = #\"clarinet\"\n\\clef \"treble_8\" \n\\key c \\major\n\\time "
            preamble += str(self._dodec.time_enumerator)
            preamble += "/"
            preamble += str(self._dodec.time_denominator)
            preamble += "\n"
        elif voice in range(5, 7):  # F clef
            preamble += "\n\\new Staff = \""
            if voice == 5:
                preamble += "Baritone\""
                preamble += "<<\n\\new Voice = \"vocal\" \\with {\n\\remove \"Forbid_line_break_engraver\"\n}\n"
                preamble += "{ \\fixed e { \n\\tempo 4 = "
            elif voice == 6:
                preamble += "Bass\""
                preamble += "<<\n\\new Voice = \"vocal\" \\with {\n\\remove \"Forbid_line_break_engraver\"\n}\n"
                preamble += "{ \\fixed c { \n\\tempo 4 = "
            preamble += str(self._dodec.tempo)
            preamble += "\n\\set midiInstrument = #\"piano\"\n\\clef \"bass\" \n\\key c \\major\n\\time "
            preamble += str(self._dodec.time_enumerator)
            preamble += "/"
            preamble += str(self._dodec.time_denominator)
            preamble += "\n"
        return preamble

    def generate_composition(self):
        print("generating composition")
        # For each voice, generate the number of repeats for the series.
        for voice in self._dodec.voices:
            self._composition += self.create_voice_preamble(voice)
            bar_count = 0
            for i in range(self._dodec.repeats):
                # Generate the repeat based on the series and the provided characteristics
                # First, determine the variation of this repeat
                variation = random.randint(0, 3)
                if variation == Variations.SERIES:
                    self._composition += self.generate_repeat(self._dodec.series)
                elif variation == Variations.INVERSE:
                    self._composition += self.generate_repeat(self._dodec.inverse)
                elif variation == Variations.RETROGRADE:
                    self._composition += self.generate_repeat(self._dodec.retrograde)
                else:  # RETROGRADEINVERSE
                    self._composition += self.generate_repeat(self._dodec.retrograde_inverse)
            self._composition += "\n} \n}\n>>\n\n"

    def generate_score(self):
        """ Generate a composition based on the settings provided. """
        self._score += "\\version \"2.20.0\"\n"
        self._score += "\\header\n{\n"
        self._score += "title = \""
        self._score += self._dodec.title
        self._score += "\"\n"
        self._score += "composer = \"Randomly generated by Dodecaphonist\"\n}\n"
        self._score += "\\score {\n{ \n<<\n"
        self._score += "\\new StaffGroup\n\\relative <<\n"
        self.generate_composition()
        self._score += self._composition
        self._score += "\n>>\n >>}\n\\midi\n{\n}\n\\layout\n{ \n}\n}\n"

    def save_lilypond_file(self):
        self._dodec.filename += '.ly'
        with open(self._path, 'w') as f:
            f.write(self._score)

    def save_other_formats(self):
        os.system('lilypond -o ' + self._dodec.foldername + ' ' + self._path)
