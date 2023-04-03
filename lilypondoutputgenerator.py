import os


class LilypondOutputGenerator:
    def __init__(self, score, foldername, path):
        self._score = score
        self._foldername = foldername
        self._path = path + '.ly'

    def save_lilypond_file(self):
        """Save the generated file to the provided path."""
        with open(self._path, 'w') as f:
            f.write(self._score)

    def save_midi_file(self):
        """Convert the generated file to PDF and MIDI by running Lilypond"""
        os.system('lilypond --midi -o ' + self._foldername + ' ' + self._path)

    def save_pdf_file(self):
        """Convert the generated file to PDF and MIDI by running Lilypond"""
        os.system('lilypond --pdf -o ' + self._foldername + ' ' + self._path)

    def save_png_file(self):
        os.system('lilypond --png -o ' + self._foldername + ' ' + self._path)
