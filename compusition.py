class Compusition():
    def __init__(self):
        title = ""              # Title of the compusition
        filename = ""           # Filename, used for ly, pdf, mid
        foldername = ""         # Save location
        notes_value = 0         # Notes percentage
        rests_value = 0         # Rests percentage
        key = 0                 # 0 is sharps, 1 is flats
        repeats = 0             # Number of times the series is repeated
        voices = 0              # Number of voices (1-6)
        time_enumerator = 0     # Beats per measure (1-12)
        time_denominator = 0    # Counting unit (1/1 - 1/32)
        tempo = 0               # Tempo (bpm)
        repeat_current = False  # Repeat current note or not
        current_chance = 0      # Repeat current note chance
        repeat_previous = False # Repeat previous note or not
        previous_chance = 0     # Repeat previous note chance

    def generate(self):
        """ Generate a compusition based on the settings provided. """
        print("generating compusition")
