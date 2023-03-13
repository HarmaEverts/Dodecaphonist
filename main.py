from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog
)
import sys
from ui_Compunist import Ui_MainWindow
from dodecaphony import Dodecaphony
from scoregenerator import ScoreGenerator
from lilypondgenerator import LilypondGenerator


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dodec = Dodecaphony()

        # SIGNALS ===============================================================================

        # Set up the UI options in drop-downs etc.
        # Compusition template:
        self.ui.composition_mode.addItems(["Select", "Schoenberg", "Webern", "Stravinsky"])
        self.ui.composition_mode.currentIndexChanged.connect(self.update_mode)

        # Key signature:
        self.ui.key.addItems(["Sharps", "Flats"])
        self.ui.key.currentIndexChanged.connect(self.update_key_signature)

        # Time signature:
        enumerator_options = range(1, 13)
        denominator_options = [1, 2, 4, 8, 16, 32]
        self.ui.time_enumerator.addItems([str(x) for x in enumerator_options])
        self.ui.time_denominator.addItems([str(x) for x in denominator_options])
        self.ui.time_enumerator.currentIndexChanged.connect(self.update_time_enumerator)
        self.ui.time_denominator.currentIndexChanged.connect(self.update_time_denominator)

        # Tempo:
        self.ui.tempo.valueChanged.connect(self.update_tempo)

        # Notes versus rests balance:
        self.ui.notes_rests_slider.valueChanged.connect(self.notes_rests_valuechange)

        # Repeat current note chance:
        self.ui.currentslider.valueChanged.connect(self.update_repeat_current_note_chance)

        # Repeat previous note or not (initially disabled):
        self.ui.previousslider.setEnabled(False)
        self.ui.previouspercentage.setEnabled(False)
        # Chance:
        self.ui.previousslider.valueChanged.connect(self.update_repeat_previous_note_chance)

        # Number of series repeats:
        self.ui.no_of_repeats.valueChanged.connect(self.update_no_of_repeats)

        # Settings for different note and rest types:
        self.ui.whole_note_slider.valueChanged.connect(self.update_whole_note)
        self.ui.dotted_whole_note_slider.valueChanged.connect(self.update_dotted_whole_note)
        self.ui.half_note_slider.valueChanged.connect(self.update_half_note)
        self.ui.dotted_half_note_slider.valueChanged.connect(self.update_dotted_half_note)
        self.ui.quarter_note_slider.valueChanged.connect(self.update_quarter_note)
        self.ui.dotted_quarter_note_slider.valueChanged.connect(self.update_dotted_quarter_note)
        self.ui.eighth_note_slider.valueChanged.connect(self.update_eighth_note)
        self.ui.dotted_eighth_note_slider.valueChanged.connect(self.update_dotted_eighth_note)
        self.ui.sixteenth_note_slider.valueChanged.connect(self.update_sixteenth_note)

        self.ui.whole_rest_slider.valueChanged.connect(self.update_whole_rest)
        self.ui.dotted_whole_rest_slider.valueChanged.connect(self.update_dotted_whole_rest)
        self.ui.half_rest_slider.valueChanged.connect(self.update_half_rest)
        self.ui.dotted_half_rest_slider.valueChanged.connect(self.update_dotted_half_rest)
        self.ui.quarter_rest_slider.valueChanged.connect(self.update_quarter_rest)
        self.ui.dotted_quarter_rest_slider.valueChanged.connect(self.update_dotted_quarter_rest)
        self.ui.eighth_rest_slider.valueChanged.connect(self.update_eighth_rest)
        self.ui.dotted_eighth_rest_slider.valueChanged.connect(self.update_dotted_eighth_rest)
        self.ui.sixteenth_rest_slider.valueChanged.connect(self.update_sixteenth_rest)

        # Select output folder:
        self.ui.open_file_explorer.clicked.connect(self.update_folder_name)

        # Generate the series:
        self.ui.generate_series.clicked.connect(self.generate_series)

        # Generate the compusition:
        self.ui.generate_score.clicked.connect(self.create_score)

        # INITIAL UI SETTINGS ==================================================

        # Set initial focus:
        self.ui.composition_mode.setFocus()

        # Enable chance of repeating current item
        self.ui.currentslider.setEnabled(True)
        self.ui.currentpercentage.setEnabled(True)

        # Disable chance of repeating previous item (until current chance is turned on)
        self.ui.previousslider.setEnabled(False)
        self.ui.previouspercentage.setEnabled(False)

        # Set drop-down options for voices:
        voice_list = ["Not set", "Soprano", "Mezzo-soprano", "Alto", "Tenor", "Baritone", "Bass"]
        self.ui.voice1.addItems(voice_list)
        self.ui.voice2.addItems(voice_list)
        self.ui.voice3.addItems(voice_list)
        self.ui.voice4.addItems(voice_list)
        self.ui.voice5.addItems(voice_list)
        self.ui.voice6.addItems(voice_list)

        # Update voices
        self.ui.voice1.currentIndexChanged.connect(self.update_voices)
        self.ui.voice2.currentIndexChanged.connect(self.update_voices)
        self.ui.voice3.currentIndexChanged.connect(self.update_voices)
        self.ui.voice4.currentIndexChanged.connect(self.update_voices)
        self.ui.voice5.currentIndexChanged.connect(self.update_voices)
        self.ui.voice6.currentIndexChanged.connect(self.update_voices)

    # SLOTS =================================================================

    def update_key_signature(self):
        self.dodec.key = self.ui.key.currentIndex()

    def update_time_enumerator(self):
        self.dodec.time_enumerator = self.ui.time_enumerator.currentIndex() + 1

    def update_time_denominator(self):
        self.dodec.time_denominator = int(self.ui.time_denominator.currentText())

    def update_tempo(self):
        self.dodec.tempo = self.ui.tempo.value()

    def update_mode(self):
        """ Updates the composition settings based on the selected mode. """
        if self.ui.composition_mode.currentIndex() == 1:
            self.apply_schoenberg_template()
        elif self.ui.composition_mode.currentIndex() == 2:
            self.apply_webern_template()
        elif self.ui.composition_mode.currentIndex() == 3:
            self.apply_stravinsky_template()

    def apply_schoenberg_template(self):
        """ Updates the composition settings and UI according to the Schoenberg template. """
        self.ui.voice1.setCurrentIndex(1)
        self.ui.voice2.setCurrentIndex(3)
        self.ui.voice3.setCurrentIndex(4)
        self.ui.voice4.setCurrentIndex(6)
        self.ui.key.setCurrentIndex(1)
        self.ui.tempo.setValue(44)
        self.ui.time_enumerator.setCurrentIndex(1)
        self.ui.time_denominator.setCurrentIndex(1)
        self.ui.notes_rests_slider.setValue(91)
        self.ui.score_title.setText("Schoenberg")
        self.ui.output_filename_2.setText("Schoenberg")
        self.ui.previousslider.setValue(0)
        self.ui.currentslider.setValue(0)
        self.ui.no_of_repeats.setValue(3)
        self.ui.half_note_slider.setValue(2)
        self.ui.quarter_note_slider.setValue(17)
        self.ui.dotted_quarter_note_slider.setValue(22)
        self.ui.eighth_note_slider.setValue(72)
        self.ui.dotted_eighth_note_slider.setValue(80)
        self.ui.sixteenth_note_slider.setValue(90)
        self.ui.half_rest_slider.setValue(92)
        self.ui.quarter_rest_slider.setValue(94)
        self.ui.eighth_rest_slider.setValue(98)
        self.ui.sixteenth_rest_slider.setValue(100)

    def apply_webern_template(self):
        """ Updates the composition settings and UI according to the Webern template. """
        print("Webern")

    def apply_stravinsky_template(self):
        """ Updates the composition settings and UI according to the Stravinsky template. """
        print("Stravinsky")

    def update_no_of_repeats(self):
        self.dodec.repeats = self.ui.no_of_repeats.value()

    def update_voices(self):
        """ Update the voices (1-6) """
        self.dodec.voices = []
        if self.ui.voice1.currentIndex() != 0:
            self.dodec.voices.append(self.ui.voice1.currentIndex())
        if self.ui.voice2.currentIndex() != 0:
            self.dodec.voices.append(self.ui.voice2.currentIndex())
        if self.ui.voice3.currentIndex() != 0:
            self.dodec.voices.append(self.ui.voice3.currentIndex())
        if self.ui.voice4.currentIndex() != 0:
            self.dodec.voices.append(self.ui.voice4.currentIndex())
        if self.ui.voice5.currentIndex() != 0:
            self.dodec.voices.append(self.ui.voice5.currentIndex())
        if self.ui.voice6.currentIndex() != 0:
            self.dodec.voices.append(self.ui.voice6.currentIndex())

        self.dodec.no_of_voices = len(self.dodec.voices)

    def notes_rests_valuechange(self):
        """ Checks the value of the notes - rests slider, and updates the notes and rests percentage labels accordingly.
        The total should always sum up to 100%. """
        self.dodec.notes_value = self.ui.notes_rests_slider.value()
        self.dodec.rests_value = 100 - self.dodec.notes_value
        self.ui.percent_notes.setText(str(self.dodec.notes_value) + " % notes")
        self.ui.percent_rests.setText(str(self.dodec.rests_value) + " % rests")

    def update_repeat_note_settings(self):
        """ Toggles the repeat current note details depending on whether the checkbox is selected. """
        if self.ui.currentslider.value() != 0:  # Current note repetition is on -> previous is enabled.
            self.ui.previouspercentage.setEnabled(True)
            self.ui.previousslider.setEnabled(True)
        else:  # Current note repetition is off -> previous must also be off.
            self.ui.previouspercentage.setEnabled(False)
            self.ui.previousslider.setEnabled(False)
            self.ui.previousslider.setValue(0)

    def update_repeat_current_note_chance(self):
        """ Updates the chance of repeating the current note. """
        self.ui.currentpercentage.setText(str(self.ui.currentslider.value()) + " %")
        self.dodec.current_chance = self.ui.currentslider.value()
        self.update_repeat_note_settings()

    def update_repeat_previous_note_chance(self):
        """ Updates the chance of repeating the previous note. """
        self.ui.previouspercentage.setText(str(self.ui.previousslider.value()) + " %")
        self.dodec.previous_chance = self.ui.previousslider.value()
        self.update_repeat_note_settings()

    def update_whole_note(self):
        self.ui.whole_note_pc.setText(str(self.ui.whole_note_slider.value()) + '%')
        self.dodec.note_chances["Whole"] = self.ui.whole_note_slider.value()

    def update_dotted_whole_note(self):
        self.ui.dotted_whole_note_pc.setText(str(self.ui.dotted_whole_note_slider.value()) + '%')
        self.dodec.note_chances["Dotted-whole"] = self.ui.dotted_whole_note_slider.value()

    def update_half_note(self):
        self.ui.half_note_pc.setText(str(self.ui.half_note_slider.value()) + '%')
        self.dodec.note_chances["Half"] = self.ui.half_note_slider.value()

    def update_dotted_half_note(self):
        self.ui.dotted_half_note_pc.setText(str(self.ui.dotted_half_note_slider.value()) + '%')
        self.dodec.note_chances["Dotted-half"] = self.ui.dotted_half_note_slider.value()

    def update_quarter_note(self):
        self.ui.quarter_note_pc.setText(str(self.ui.quarter_note_slider.value()) + '%')
        self.dodec.note_chances["Quarter"] = self.ui.quarter_note_slider.value()

    def update_dotted_quarter_note(self):
        self.ui.dotted_quarter_note_pc.setText(str(self.ui.dotted_quarter_note_slider.value()) + '%')
        self.dodec.note_chances["Dotted-quarter"] = self.ui.dotted_quarter_note_slider.value()

    def update_eighth_note(self):
        self.ui.eighth_note_pc.setText(str(self.ui.eighth_note_slider.value()) + '%')
        self.dodec.note_chances["Eighth"] = self.ui.eighth_note_slider.value()

    def update_dotted_eighth_note(self):
        self.ui.dotted_eighth_note_pc.setText(str(self.ui.dotted_eighth_note_slider.value()) + '%')
        self.dodec.note_chances["Dotted-eighth"] = self.ui.dotted_eighth_note_slider.value()

    def update_sixteenth_note(self):
        self.ui.sixteenth_note_pc.setText(str(self.ui.sixteenth_note_slider.value()) + '%')
        self.dodec.note_chances["Sixteenth"] = self.ui.sixteenth_note_slider.value()

    def update_whole_rest(self):
        self.ui.whole_rest_pc.setText(str(self.ui.whole_rest_slider.value()) + '%')
        self.dodec.rest_chances["Whole"] = self.ui.whole_rest_slider.value()

    def update_dotted_whole_rest(self):
        self.ui.dotted_whole_rest_pc.setText(str(self.ui.dotted_whole_rest_slider.value()) + '%')
        self.dodec.rest_chances["Dotted-whole"] = self.ui.dotted_whole_rest_slider.value()

    def update_half_rest(self):
        self.ui.half_rest_pc.setText(str(self.ui.half_rest_slider.value()) + '%')
        self.dodec.rest_chances["Half"] = self.ui.half_rest_slider.value()

    def update_dotted_half_rest(self):
        self.ui.dotted_half_rest_pc.setText(str(self.ui.dotted_half_rest_slider.value()) + '%')
        self.dodec.rest_chances["Dotted-half"] = self.ui.dotted_half_rest_slider.value()

    def update_quarter_rest(self):
        self.ui.quarter_rest_pc.setText(str(self.ui.quarter_rest_slider.value()) + '%')
        self.dodec.rest_chances["Quarter"] = self.ui.quarter_rest_slider.value()

    def update_dotted_quarter_rest(self):
        self.ui.dotted_quarter_rest_pc.setText(str(self.ui.dotted_quarter_rest_slider.value()) + '%')
        self.dodec.rest_chances["Dotted-quarter"] = self.ui.dotted_quarter_rest_slider.value()

    def update_eighth_rest(self):
        self.ui.eighth_rest_pc.setText(str(self.ui.eighth_rest_slider.value()) + '%')
        self.dodec.rest_chances["Eighth"] = self.ui.eighth_rest_slider.value()

    def update_dotted_eighth_rest(self):
        self.ui.dotted_eighth_rest_labe.setText(str(self.ui.dotted_eighth_rest_slider.value()) + '%')
        self.dodec.rest_chances["Dotted-eighth"] = self.ui.dotted_eighth_rest_slider.value()

    def update_sixteenth_rest(self):
        self.ui.sixteenth_rest_pc.setText(str(self.ui.sixteenth_rest_slider.value()) + '%')
        self.dodec.rest_chances["Sixteenth"] = self.ui.sixteenth_rest_slider.value()

    def update_folder_name(self):
        """ Selects the folder in which the generated files will be saved. """
        foldername = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.output_foldername.setText(foldername)

    # OTHER FUNCTIONS ============================================================================

    def update_from_ui(self):
        """ Get all current UI settings and update the Dodecaphony object accordingly """
        self.dodec.key = self.ui.key.currentIndex()
        self.dodec.time_enumerator = int(self.ui.time_enumerator.currentText())
        self.dodec.time_denominator = int(self.ui.time_denominator.currentText())
        self.dodec.repeats = self.ui.no_of_repeats.value()
        self.update_voices()
        self.dodec.tempo = self.ui.tempo.value()
        self.dodec.notes_value = self.ui.notes_rests_slider.value()
        self.dodec.rests_value = 100 - self.dodec.notes_value
        self.dodec.repeat_current = self.ui.currentslider.value() != 0  # Remove
        self.dodec.current_chance = self.ui.currentslider.value()
        self.dodec.repeat_previous = self.ui.currentslider.value() != 0  # Remove
        self.dodec.previous_chance = self.ui.previousslider.value()
        self.dodec.note_chances["Whole"] = self.ui.whole_note_slider.value()
        self.dodec.note_chances["Dotted-whole"] = self.ui.dotted_whole_note_slider.value()
        self.dodec.note_chances["Half"] = self.ui.half_note_slider.value()
        self.dodec.note_chances["Dotted-half"] = self.ui.dotted_half_note_slider.value()
        self.dodec.note_chances["Quarter"] = self.ui.quarter_note_slider.value()
        self.dodec.note_chances["Dotted-quarter"] = self.ui.dotted_quarter_note_slider.value()
        self.dodec.note_chances["Eighth"] = self.ui.eighth_note_slider.value()
        self.dodec.note_chances["Dotted-eighth"] = self.ui.dotted_eighth_note_slider.value()
        self.dodec.note_chances["Sixteenth"] = self.ui.sixteenth_note_slider.value()
        self.dodec.rest_chances["Whole"] = self.ui.whole_rest_slider.value()
        self.dodec.rest_chances["Dotted-whole"] = self.ui.dotted_whole_rest_slider.value()
        self.dodec.rest_chances["Half"] = self.ui.half_rest_slider.value()
        self.dodec.rest_chances["Dotted-half"] = self.ui.dotted_half_rest_slider.value()
        self.dodec.rest_chances["Quarter"] = self.ui.quarter_rest_slider.value()
        self.dodec.rest_chances["Dotted-quarter"] = self.ui.dotted_quarter_rest_slider.value()
        self.dodec.rest_chances["Eighth"] = self.ui.eighth_rest_slider.value()
        self.dodec.rest_chances["Dotted-eighth"] = self.ui.dotted_eighth_rest_slider.value()
        self.dodec.rest_chances["Sixteenth"] = self.ui.sixteenth_rest_slider.value()
        self.dodec.title = self.ui.score_title.text()
        self.dodec.filename = self.ui.output_filename_2.text()
        self.dodec.foldername = self.ui.output_foldername.text()

    def validate_settings(self):
        """ Validate the provided input settings.
        :return: True if the settings are valid
        :return: False if the settings are not valid """
        # First, make sure that all UI settings are registered.
        self.update_from_ui()
        self.dodec.validate()
        return True

    def generate_series(self):
        if self.validate_settings():
            self.dodec.generate_series()
            self.ui.generate_series.setText("Regenerate series")
            self.ui.series_preview.setText(str(self.dodec.series))
        else:
            print("Invalid settings, cannot generate series.")

    def create_score(self):
        """ Creates a Dodecaphony object based on the provided settings and outputs the generated composition
        to the specified folder with the filename as its name. """
        if self.validate_settings():
            self.dodec.generate_series()
            score_generator = ScoreGenerator(self.dodec)
            score_generator.generate_composition()
            lilypond_generator = LilypondGenerator(score_generator.Composition, score_generator._dodec.tempo, score_generator._dodec.time_enumerator, score_generator._dodec.time_denominator, score_generator._dodec.foldername, score_generator._path, score_generator._dodec.title)
            lilypond_generator.generate_files()
        else:
            print("Invalid settings, cannot generate score.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
