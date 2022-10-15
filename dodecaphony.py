class Dodecaphony():
    def __init__(self):
        self.title = ""              # Title of the compusition
        self.filename = ""           # Filename, used for ly, pdf, mid
        self.foldername = ""         # Save location
        self.notes_value = 0         # Notes percentage
        self.rests_value = 0         # Rests percentage
        self.key = 0                 # 0 is sharps, 1 is flats
        self.repeats = 0             # Number of times the series is repeated
        self.no_of_voices = 0        # Number of voices (1-6)
        self.voices = []             # List of voice types, one for each voice (0 is not set!)
        self.time_enumerator = 0     # Beats per measure (1-12)
        self.time_denominator = 0    # Counting unit (1/1 - 1/32)
        self.tempo = 0               # Tempo (bpm)
        self.current_chance = 0      # Repeat current note chance
        self.previous_chance = 0     # Repeat previous note chance
        self.series = []
        self.retrograde = []
        self.inverse = []
        self.retrogradeinverse = []
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


    def generate_series(self):
        """ Generate a random dodecaphony series and its variations """
        print("generating series")


    def generate_score(self):
        """ Generate a compusition based on the settings provided. """
        print("generating compusition")
