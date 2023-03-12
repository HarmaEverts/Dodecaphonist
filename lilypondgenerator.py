import scoregenerator
import score_element
from score_element import ElementType
import os


class LilypondGenerator:
    def __init__(self, composition, tempo, time_enumerator, time_denominator, foldername, path, title):
        self._composition = composition
        self._tempo = tempo
        self._time_enumerator = time_enumerator
        self._time_denominator = time_denominator
        self._bar_length = time_enumerator * (16/time_denominator)
        self._foldername = foldername
        self._path = path + '.ly'
        self._title = title
        self._score = ''
        self._lengths_ly = {24: "1.",
                            16: "1",
                            14: "2..",
                            12: "2.",
                            8: "2",
                            7: "4..",
                            6: "4.",
                            4: "4",
                            3: "8.",
                            2: "8",
                            1: "16"}
        # Lilypond lengths, counted from whole note, dotted whole note to sixteenth note.

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
            tempo = str(self._tempo)
            preamble += tempo
            preamble += "\n\\set midiInstrument = #\"flute\"\n\\clef \"treble\" \n\\key c \\major\n\\time "
            preamble += str(self._time_enumerator)
            preamble += "/"
            preamble += str(self._time_denominator)
            preamble += "\n"
        elif voice == 4:  # G clef octave down
            preamble += "\n\\new Staff = \"Tenor\""
            preamble += "<<\n\\new Voice = \"vocal\" \\with {\n\\remove \"Forbid_line_break_engraver\"\n}\n"
            preamble += "{ \\fixed g { \n\\tempo 4 = "
            preamble += str(self._tempo)
            preamble += "\n\\set midiInstrument = #\"clarinet\"\n\\clef \"treble_8\" \n\\key c \\major\n\\time "
            preamble += str(self._time_enumerator)
            preamble += "/"
            preamble += str(self._time_denominator)
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
            preamble += str(self._tempo)
            preamble += "\n\\set midiInstrument = #\"piano\"\n\\clef \"bass\" \n\\key c \\major\n\\time "
            preamble += str(self._time_enumerator)
            preamble += "/"
            preamble += str(self._time_denominator)
            preamble += "\n"
        return preamble

    def convert_score_element_to_lilypond(self, current_score_element: score_element):
        result = ''
        result += current_score_element.get_pitch()
        result += self._lengths_ly[current_score_element.get_length()]
        result += ' '
        return result

    def split_items(self, length):
        if length == 5:
            return 4, 1
        elif length == 9:
            return 8, 1
        elif length == 10:
            return 8, 2
        elif length == 11:
            return 8, 3
        elif length == 13:
            return 12, 1
        elif length == 15:
            return 12, 3
        elif length == 17:
            return 14, 3
        elif length == 18:
            return 12, 6
        elif length == 19:
            return 16, 3
        elif length == 20:
            return 16, 4
        elif length == 21:
            return 16, 4, 1
        elif length == 22:
            return 16, 4, 2
        elif length == 23:
            return 16, 4, 3

    def split(self, current_score_element, remainder):
        item_length = current_score_element.get_length()
        second_part = item_length - remainder
        first_part = item_length - second_part
        element = current_score_element.get_pitch()
        result = ''
        if first_part in self._lengths_ly:
            result = element + self._lengths_ly[first_part] + '~ '
        else:
            split_items = self.split_items(first_part)
            for item in split_items:
                result += element + self._lengths_ly[item] + '~ '
            result = result[:-2]
            result += ' '
        if second_part in self._lengths_ly:
            result += element + self._lengths_ly[second_part] + ' '
        else:
            split_items = self.split_items(second_part)
            for item in split_items:
                result += element + self._lengths_ly[item] + '~ '
            result = result[:-2]
            result += ' '
        return result

    def convert_melody_to_lilypond(self, melody):
        converted_melody = ""
        current_bar_length = 0
        for item in melody:
            new_bar_length = current_bar_length + item.get_length()
            if new_bar_length > self._bar_length:
                converted_melody += self.split(item, new_bar_length - self._bar_length)
                current_bar_length = new_bar_length % self._bar_length
            elif new_bar_length == self._bar_length:
                converted_melody += self.convert_score_element_to_lilypond(item)
                current_bar_length = 0
            else:
                converted_melody += self.convert_score_element_to_lilypond(item)
                current_bar_length = new_bar_length
        return converted_melody

    def generate_score(self):
        """ Generate a composition based on the settings provided. """
        self._score += "\\version \"2.20.0\"\n"
        self._score += "\\header\n{\n"
        self._score += "title = \""
        self._score += self._title
        self._score += "\"\n"
        self._score += "composer = \"Randomly generated by Dodecaphonist\"\n}\n"
        self._score += "\\score {\n{ \n<<\n"
        self._score += "\\new StaffGroup\n\\relative <<\n"
        voices = self._composition.get_voices()
        for voice in voices:
            self._score += self.create_voice_preamble(voice.get_voice_type())
            self._score += self.convert_melody_to_lilypond(voice.get_melody())
            self._score += "\n} \n}\n>>\n\n"
        self._score += "\n>>\n >>}\n\\midi\n{\n}\n\\layout\n{ \n}\n}\n"

    def save_lilypond_file(self):
        with open(self._path, 'w') as f:
            f.write(self._score)

    def save_other_formats(self):
        os.system('lilypond -o ' + self._foldername + ' ' + self._path)

    def generate_files(self):
        self.generate_score()
        self.save_lilypond_file()
        self.save_other_formats()


