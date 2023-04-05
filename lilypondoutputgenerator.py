import os
from PIL import Image


class LilypondOutputGenerator:
    def __init__(self, score, foldername, path):
        self._score = score
        self._foldername = foldername
        self._path = path + '.ly'

    def save_lilypond_file(self):
        """Save the generated file to the provided path."""
        with open(self._path, 'w') as f:
            f.write(self._score)

    def save_pdf_file(self):
        """Convert the generated file to PDF and MIDI by running Lilypond"""
        os.system('lilypond --pdf -o ' + self._foldername + ' ' + self._path)

    def save_png_file(self):
        os.system('lilypond --png -o ' + self._foldername + ' ' + self._path)

    def save_preview_png(self, path):
        preview_image_path = path + '.png'
        preview_image = Image.open(preview_image_path)
        preview_image_cropped = preview_image.crop((96, 0, 688, 110))
        preview_image_cropped.save(path + '_cropped.png')
        return path + '_cropped.png'

    def save_all_filetypes(self):
        self.save_lilypond_file()
        self.save_pdf_file()
        self.save_png_file()
