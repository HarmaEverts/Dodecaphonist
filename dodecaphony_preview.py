import os.path


class DodecaphonyPreview:
    def __init__(self, filename, foldername, series):
        self.title = ""              # Title of the composition
        self.filename = filename     # Filename, used for ly, pdf, mid
        self.foldername = foldername # Save location
        self.path = os.path.join(foldername, filename)               # Full path to preview file (folder + file)
        self.time_enumerator = 12    # Count per measure (1-12)
        self.time_denominator = 1    # Counting unit (1/1 - 1/32)

        self.series = series
