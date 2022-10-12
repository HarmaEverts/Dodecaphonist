class Dodecaphony():
    def __init__(self):
        self.title = ""              # Title of the compusition
        self.filename = ""           # Filename, used for ly, pdf, mid
        self.foldername = ""         # Save location
        self.notes_value = 0         # Notes percentage
        self.rests_value = 0         # Rests percentage
        self.key = 0                 # 0 is sharps, 1 is flats
        self.repeats = 0             # Number of times the series is repeated
        self.voices = 0              # Number of voices (1-6)
        self.voices = []             # List of voice types, one for each voice
        self.time_enumerator = 0     # Beats per measure (1-12)
        self.time_denominator = 0    # Counting unit (1/1 - 1/32)
        self.tempo = 0               # Tempo (bpm)
        self.repeat_current = False  # Repeat current note or not
        self.current_chance = 0      # Repeat current note chance
        self.repeat_previous = False # Repeat previous note or not
        self.previous_chance = 0     # Repeat previous note chance
        self.series = []
        self.retrograde = []
        self.inverse = []
        self.retrogradeinverse = []


    def generate(self):
        """ Generate a compusition based on the settings provided. """
        print("generating compusition")
