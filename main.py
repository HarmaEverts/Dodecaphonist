from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QApplication
, QMainWindow, QFileDialog
)
import sys
from ui_Compunist import Ui_MainWindow
from dodecaphony import Dodecaphony


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dodec = Dodecaphony()

    # SIGNALS ===============================================================================

        # Set up the UI options in drop-downs etc.
        # Compusition template:
        self.ui.composition_mode.addItems(["Schoenberg", "Webern", "Stravinsky"])
        self.ui.composition_mode.currentIndexChanged.connect(self.update_mode)

        # Series repeats:
        self.ui.no_of_repeats.valueChanged.connect(self.update_repeats)

        # Voices:
        self.ui.no_of_voices.valueChanged.connect(self.update_voices)

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

        # Repeat current note or not:
        self.ui.repeat_current_note.stateChanged.connect(self.toggle_repeat_current_note)
        # Chance:
        self.ui.currentslider.valueChanged.connect(self.update_repeat_current_note_chance)

        # Repeat previous note or not (initially disabled):
        self.ui.repeat_previous_note.setEnabled(False)
        self.ui.repeat_previous_note.stateChanged.connect(self.toggle_repeat_previous_note)
        # Chance:
        self.ui.previousslider.valueChanged.connect(self.update_repeat_previous_note_chance)

        # Set the score title:
        self.ui.score_title.textChanged.connect(self.update_score_title)

        # Set the filename (.ly, .pdf, .mid)
        self.ui.output_filename_2.textChanged.connect(self.update_filename)

        # Select output folder:
        self.ui.open_file_explorer.clicked.connect(self.update_folder_name)

        # Generate the compusition:
        self.ui.generate_score.clicked.connect(self.create_score)

    # INITIAL UI SETTINGS ==================================================+

        # Set initial focus:
        self.ui.composition_mode.setFocus()

        # Hide extra voices and their labels:
        self.ui.voice2.hide()
        self.ui.voice3.hide()
        self.ui.voice4.hide()
        self.ui.voice5.hide()
        self.ui.voice6.hide()

        self.ui.voice2label.hide()
        self.ui.voice3label.hide()
        self.ui.voice4label.hide()
        self.ui.voice5label.hide()
        self.ui.voice6label.hide()

        # Set drop-down options for voices:
        voice_list = ["Soprano", "Mezzo-soprano", "Alto", "Tenor", "Baritone", "Bass"]
        self.ui.voice1.addItems(voice_list)
        self.ui.voice2.addItems(voice_list)
        self.ui.voice3.addItems(voice_list)
        self.ui.voice4.addItems(voice_list)
        self.ui.voice5.addItems(voice_list)
        self.ui.voice6.addItems(voice_list)

    # SLOTS =================================================================
    def update_mode(self):
        """
        Updates the composition settings based on the selected mode.
        """
        if self.ui.composition_mode.currentIndex() == 0:
            self.apply_schoenberg_template()
        elif self.ui.composition_mode.currentIndex() == 1:
            self.apply_webern_template()
        elif self.ui.composition_mode.currentIndex() == 2:
            self.apply_stravinsky_template()

    def apply_schoenberg_template(self):
        """ Updates the composition settings and UI according to the Schoenberg template. """
        print("Schoenberg")

    def apply_webern_template(self):
        """ Updates the composition settings and UI according to the Webern template. """
        print("Webern")

    def apply_stravinsky_template(self):
        """ Updates the composition settings and UI according to the Stravinsky template. """
        print("Stravinsky")

    def update_repeats(self):
        """ Updates the number of repeats of the series """
        self.dodec.repeats = self.ui.no_of_repeats.value()

    def update_voices(self):
        """ Update the number of voices (1-6) """
        self.dodec.voices = self.ui.no_of_voices.value()
        # TODO Show all applicable voices and process their inputs.

    def update_key_signature(self):
        """ Toggles between sharps and flats depending on the selection in the drop-down list.
        0 is sharps, 1 is flats. """
        self.dodec.key = self.ui.key.currentIndex()

    def update_time_enumerator(self):
        """ Set the number of beats per measure (1-12). """
        self.dodec.time_enumerator = self.ui.time_enumerator.currentIndex() + 1

    def update_time_denominator(self):
        """ Set the type of note to count with (1/1, 1/2, 1/4, 1/8, 1/16, 1/32).
        Contains one number (the denominator, the enumerator is stored in time_enumerator) """
        self.dodec.time_denominator = int(self.ui.time_denominator.currentText())

    def update_tempo(self):
        """ Set the tempo for the piece in beats per minute. """
        self.dodec.tempo = self.ui.tempo.value()

    def notes_rests_valuechange(self):
        """ Checks the value of the notes - rests slider, and updates the notes and rests percentage labels accordingly.
        The total should always sum up to 100%. """
        self.dodec.notes_value = self.ui.notes_rests_slider.value()
        self.dodec.rests_value = 100 - self.dodec.notes_value
        self.ui.percent_notes.setText(str(self.dodec.notes_value) + " % notes")
        self.ui.percent_rests.setText(str(self.dodec.rests_value) + " % rests")

    def toggle_repeat_current_note(self):
        """ Toggles the repeat current note details depending on whether the checkbox is selected. """
        self.ui.currentlabel.setEnabled(self.ui.repeat_current_note.isChecked())
        self.ui.currentslider.setEnabled(self.ui.repeat_current_note.isChecked())
        self.ui.currentpercentage.setEnabled(self.ui.repeat_current_note.isChecked())
        self.dodec.repeat_current = self.ui.repeat_current_note.isChecked()

        if not self.ui.repeat_current_note.isChecked():
            self.ui.repeat_previous_note.setChecked(False)
            self.toggle_repeat_previous_note()
            self.ui.repeat_previous_note.setEnabled(False)
        else:
            self.ui.repeat_previous_note.setEnabled(True)

    def update_repeat_current_note_chance(self):
        """ Updates the chance of repeating the current note. """
        self.dodec.current_chance = self.ui.currentslider.value()
        self.ui.currentpercentage.setText(str(self.dodec.current_chance) + " %")

    def toggle_repeat_previous_note(self):
        """ Toggles the repeat previous note details depending on whether the checkbox is selected."""
        self.ui.previouslabel.setEnabled(self.ui.repeat_previous_note.isChecked())
        self.ui.previousslider.setEnabled(self.ui.repeat_previous_note.isChecked())
        self.ui.previouspercentage.setEnabled(self.ui.repeat_previous_note.isChecked())
        self.dodec.repeat_previous = self.ui.repeat_previous_note.isChecked()

    def update_repeat_previous_note_chance(self):
        """ Updates the chance of repeating the previous note. """
        self.dodec.previous_chance = self.ui.previousslider.value()
        self.ui.previouspercentage.setText(str(self.dodec.previous_chance) + " %")

    def update_score_title(self):
        """ Update the title of the compusition """
        self.dodec.title = self.ui.score_title.text()

    def update_filename(self):
        """ Set the filename for the output file. All generated files will have the same filename,
        with a different extension for each type (.ly, .pdf, .mid). """
        self.dodec.filename = self.ui.output_filename_2.text()

    def update_folder_name(self):
        """ Selects the folder in which the generated files will be saved. """
        self.dodec.foldername = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.output_foldername.setText(self.dodec.foldername)

    # OTHER FUNCTIONS ============================================================================

    def get_folder_name(self):
        """ Retrieve the selected folder name from the UI """
        self.dodec.foldername = self.ui.output_foldername.text()

    def update_from_UI(self):
        """ Get all current UI settings and update the compositon object accordingly """
        self.update_key_signature()
        self.update_time_enumerator()
        self.update_time_denominator()
        self.update_repeats()
        self.update_voices()
        self.update_tempo()
        self.update_repeat_current_note_chance()
        self.update_repeat_previous_note_chance()
        self.update_score_title()
        self.update_filename()
        self.get_folder_name()

    def validate_settings(self):
        """ Validate the provided input settings.
        :return: True if the settings are valid
        :return: False if the settings are not valid """
        # First, make sure that all UI settings are registered.
        self.update_from_UI()

        return True

    def create_score(self):
        """ Creates a Dodecaphony object based on the provided settings and outputs the generated composition
        to the specified folder with the filename as its name. """
        if self.validate_settings():
            self.dodec.generate()
        else:
            print("Invalid settings.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
