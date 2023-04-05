import dodecaphony_preview


class LilypondPreviewGenerator:
    def __init__(self, dodec_preview: dodecaphony_preview.DodecaphonyPreview):
        self._composition = dodec_preview.series
        self._time_enumerator = dodec_preview.time_enumerator
        self._time_denominator = dodec_preview.time_denominator
        self._title = dodec_preview.title
        self._score = ''

    def convert_melody_to_lilypond(self, melody):
        """Convert the provided melody to Lilypond syntax.
        The preview only contains whole notes and no rests."""
        converted_melody = ""
        for note in melody:
            converted_melody += note
            converted_melody += '1 '
        return converted_melody

    def generate_preview(self):
        self._score += "\\version \"2.20.0\"\n"
        self._score += "\\header\n{\n}"
        self._score += "\\score {\n{ \n<<\n"
        self._score += "\\new StaffGroup\n\\relative <<\n"
        self._score += "\n\\new Staff = \""
        self._score += "Soprano\" "
        self._score += "<<\n\\new Voice = \"vocal\" \\with {\n\\remove \"Forbid_line_break_engraver\"\n}\n"
        self._score += "{ \\fixed g' { \n"
        self._score += "\n\\set midiInstrument = #\"flute\"\n\\clef \"treble\" \n\\key c \\major\n\\time "
        self._score += str(self._time_enumerator)
        self._score += "/"
        self._score += str(self._time_denominator)
        self._score += "\n"
        self._score += self.convert_melody_to_lilypond(self._composition)
        self._score += "\n} \n}\n>>\n\n"
        self._score += "\n>>\n >>}\n\\midi\n{\n}\n\\layout\n{ \n}\n}\n"


    def get_score(self):
        return self._score
