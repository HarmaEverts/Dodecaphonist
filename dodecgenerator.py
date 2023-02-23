import os


class DodecGenerator():
    def __init__(self, dodec):
        self._dodec = dodec
        self._score = ""

    def generate_score(self):
        """ Generate a composition based on the settings provided. """
        print("generating composition")
        self._score = ""

    def save_lilypond_file(self):
        path = os.path.join(self._dodec.foldername, self._dodec.filename)
        with open(path, 'w', 'utf-8') as f:
            f.write(self._score)
