import random

class Dodecaphony:
    def __init__(self):
        self.title = ""              # Title of the composition
        self.filename = ""           # Filename, used for ly, pdf, mid
        self.foldername = ""         # Save location
        self.notes_value = 0         # Notes percentage
        self.rests_value = 0         # Rests percentage
        self.key = 0                 # 0 is sharps, 1 is flats
        self.repeats = 0             # Number of times the series is repeated
        self.no_of_voices = 0        # Number of voices (1-6)
        self.voices = []             # List of voice types, one for each voice (0 is not set!)
        self.time_enumerator = 0     # Count per measure (1-12)
        self.time_denominator = 0    # Counting unit (1/1 - 1/32)
        self.tempo = 0               # Tempo (bpm)
        self.current_chance = 0      # Repeat current note chance
        self.previous_chance = 0     # Repeat previous note chance

        self.series = []
        self.retrograde = []
        self.inverse = []
        self.retrograde_inverse = []

        self.log = []

        self.note_chances = {"Whole": 0,
                             "Dotted-whole": 0,
                             "Half": 0,
                             "Dotted-half": 0,
                             "Quarter": 0,
                             "Dotted-quarter": 0,
                             "Eighth": 0,
                             "Dotted-eighth": 0,
                             "Sixteenth": 0}
        self.rest_chances = {"Whole": 0,
                             "Dotted-whole": 0,
                             "Half": 0,
                             "Dotted-half": 0,
                             "Quarter": 0,
                             "Dotted-quarter": 0,
                             "Eighth": 0,
                             "Dotted-eighth": 0,
                             "Sixteenth": 0}

        self.sharp_reflections = {'b': 'b',
                                  'c': 'ais',
                                  'cis': 'a',
                                  'd': 'gis',
                                  'dis': 'g',
                                  'e': 'fis',
                                  'f': 'f',
                                  'fis': 'e',
                                  'g': 'dis',
                                  'gis': 'd',
                                  'a': 'cis',
                                  'ais': 'c'}
        self.flat_reflections = {'b': 'b',
                                 'c': 'bes',
                                 'des': 'a',
                                 'd': 'aes',
                                 'es': 'g',
                                 'e': 'ges',
                                 'f': 'f',
                                 'ges': 'e',
                                 'g': 'es',
                                 'aes': 'd',
                                 'a': 'des',
                                 'bes': 'c'}

    def generate_series(self):
        """ Generate a random dodecaphony series and its variations """
        self.series = []
        if self.key == 0:  # sharps
            self.series = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
        else:  # flats
            self.series = ['c', 'des', 'd', 'es', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b']
        random.shuffle(self.series)
        self.update_variations()

    def update_variations(self):
        self.retrograde = list(reversed(self.series))
        self.inverse = []
        self.retrograde_inverse = []
        if self.key == 0:
            for note in self.series:
                self.inverse.append(self.sharp_reflections[note])
        else:
            for note in self.series:
                self.inverse.append(self.flat_reflections[note])
        self.retrograde_inverse = list(reversed(self.inverse))

    def add_to_log(self, log_message):
        self.log.append(log_message)

    def validate(self):
        print("validating")
        valid = True
        if self.title == "":
            self.add_to_log("You have not entered a title for your composition.")
            valid = False
        if self.filename == "":
            self.add_to_log("You have not entered a filename for your composition.")
            valid = False
        if self.foldername == "":
            self.add_to_log("You have not selected a location where to save your composition.")
            valid = False
        if self.no_of_voices == 0:
            self.add_to_log("You need at least one voice to create a composition.")
            valid = False
        if len(self.voices) == 0:
            self.add_to_log("You need at least one voice to create a composition.")
            valid = False
        if self.time_enumerator == 0:
            self.add_to_log("You have not set the time enumerator.")
            valid = False
        if self.time_denominator == 0:
            self.add_to_log("You have not set the time denominator.")
            valid = False
        if self.tempo == 0:
            self.add_to_log("You have not set a tempo.")
            valid = False

        if len(self.series) == 0:
            self.add_to_log("You have not generated a dodecaphony series yet.")
            valid = False
        if len(self.retrograde) == 0:
            self.add_to_log("You have not generated a dodecaphony series yet.")
            valid = False
        if len(self.inverse) == 0:
            self.add_to_log("You have not generated a dodecaphony series yet.")
            valid = False
        if len(self.retrograde_inverse) == 0:
            self.add_to_log("You have not generated a dodecaphony series yet.")
            valid = False

        return valid
