from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog
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
        self.ui.composition_mode.addItems(["Select", "Schoenberg", "Webern", "Stravinsky"])
        self.ui.composition_mode.currentIndexChanged.connect(self.update_mode)

        # Voices:
        self.ui.no_of_voices.valueChanged.connect(self.update_voices)

        # Key signature:
        self.ui.key.addItems(["Sharps", "Flats"])

        # Time signature:
        enumerator_options = range(1, 13)
        denominator_options = [1, 2, 4, 8, 16, 32]
        self.ui.time_enumerator.addItems([str(x) for x in enumerator_options])
        self.ui.time_denominator.addItems([str(x) for x in denominator_options])

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

        # Select output folder:
        self.ui.open_file_explorer.clicked.connect(self.update_folder_name)

        # Generate the compusition:
        self.ui.generate_score.clicked.connect(self.create_score)

    # INITIAL UI SETTINGS ==================================================+

        # Set initial focus:
        self.ui.composition_mode.setFocus()

        # Hide extra voices and their labels:
        self.ui.v2.hide()
        self.ui.v3_2.hide()
        self.ui.v4_2.hide()
        self.ui.v5_2.hide()
        self.ui.v6_2.hide()

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
        if self.ui.composition_mode.currentIndex() == 1:
            self.apply_schoenberg_template()
        elif self.ui.composition_mode.currentIndex() == 2:
            self.apply_webern_template()
        elif self.ui.composition_mode.currentIndex() == 3:
            self.apply_stravinsky_template()

    def apply_schoenberg_template(self):
        """ Updates the composition settings and UI according to the Schoenberg template. """
        self.ui.no_of_voices.setValue(4)
        self.ui.voice1.setCurrentIndex(0)
        self.ui.voice2.setCurrentIndex(2)
        self.ui.voice3.setCurrentIndex(3)
        self.ui.voice4.setCurrentIndex(5)
        self.ui.key.setCurrentIndex(1)
        self.ui.tempo.setValue(44)
        self.ui.time_enumerator.setCurrentIndex(1)
        self.ui.time_denominator.setCurrentIndex(1)
        self.ui.notes_rests_slider.setValue(91)
        self.ui.score_title.setText("Schoenberg")
        self.ui.output_filename_2.setText("Schoenberg")
        self.ui.repeat_previous_note.setEnabled(False)
        self.ui.repeat_current_note.setEnabled(False)
        self.ui.previousslider.setValue(0)
        self.ui.currentslider.setValue(0)
        self.ui.no_of_repeats.setValue(3)

    def apply_webern_template(self):
        """ Updates the composition settings and UI according to the Webern template. """
        print("Webern")

    def apply_stravinsky_template(self):
        """ Updates the composition settings and UI according to the Stravinsky template. """
        print("Stravinsky")

    def update_voices(self):
        """ Update the number of voices (1-6) """
        voices = self.ui.no_of_voices.value()

        if voices == 1:
            self.ui.v1.show()
            self.ui.v2.hide()
            self.ui.v3_2.hide()
            self.ui.v4_2.hide()
            self.ui.v5_2.hide()
            self.ui.v6_2.hide()
        elif voices == 2:
            self.ui.v1.show()
            self.ui.v2.show()
            self.ui.v3_2.hide()
            self.ui.v4_2.hide()
            self.ui.v5_2.hide()
            self.ui.v6_2.hide()
        elif voices == 3:
            self.ui.v1.show()
            self.ui.v2.show()
            self.ui.v3_2.show()
            self.ui.v4_2.hide()
            self.ui.v5_2.hide()
            self.ui.v6_2.hide()
        elif voices == 4:
            self.ui.v1.show()
            self.ui.v2.show()
            self.ui.v3_2.show()
            self.ui.v4_2.show()
            self.ui.v5_2.hide()
            self.ui.v6_2.hide()
        elif voices == 5:
            self.ui.v1.show()
            self.ui.v2.show()
            self.ui.v3_2.show()
            self.ui.v4_2.show()
            self.ui.v5_2.show()
            self.ui.v6_2.hide()
        elif voices == 6:
            self.ui.v1.show()
            self.ui.v2.show()
            self.ui.v3_2.show()
            self.ui.v4_2.show()
            self.ui.v5_2.show()
            self.ui.v6_2.show()

    def notes_rests_valuechange(self):
        """ Checks the value of the notes - rests slider, and updates the notes and rests percentage labels accordingly.
        The total should always sum up to 100%. """
        notes_value = self.ui.notes_rests_slider.value()
        rests_value = 100 - notes_value
        self.ui.percent_notes.setText(str(notes_value) + " % notes")
        self.ui.percent_rests.setText(str(rests_value) + " % rests")

    def toggle_repeat_current_note(self):
        """ Toggles the repeat current note details depending on whether the checkbox is selected. """
        self.ui.currentlabel.setEnabled(self.ui.repeat_current_note.isChecked())
        self.ui.currentslider.setEnabled(self.ui.repeat_current_note.isChecked())
        self.ui.currentpercentage.setEnabled(self.ui.repeat_current_note.isChecked())

        if not self.ui.repeat_current_note.isChecked():
            self.ui.repeat_previous_note.setChecked(False)
            self.toggle_repeat_previous_note()
            self.ui.repeat_previous_note.setEnabled(False)
        else:
            self.ui.repeat_previous_note.setEnabled(True)

    def update_repeat_current_note_chance(self):
        """ Updates the chance of repeating the current note. """
        self.ui.currentpercentage.setText(str(self.ui.currentslider.value()) + " %")

    def toggle_repeat_previous_note(self):
        """ Toggles the repeat previous note details depending on whether the checkbox is selected."""
        self.ui.previouslabel.setEnabled(self.ui.repeat_previous_note.isChecked())
        self.ui.previousslider.setEnabled(self.ui.repeat_previous_note.isChecked())
        self.ui.previouspercentage.setEnabled(self.ui.repeat_previous_note.isChecked())

    def update_repeat_previous_note_chance(self):
        """ Updates the chance of repeating the previous note. """
        self.ui.previouspercentage.setText(str(self.ui.previousslider.value()) + " %")

    def update_folder_name(self):
        """ Selects the folder in which the generated files will be saved. """
        foldername = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.output_foldername.setText(foldername)

    # OTHER FUNCTIONS ============================================================================

    def update_from_ui(self):
        """ Get all current UI settings and update the Dodecaphony object accordingly """
        self.dodec.key = self.ui.key.currentIndex()
        self.dodec.time_enumerator = self.ui.time_enumerator.currentIndex() + 1
        self.dodec.time_denominator = int(self.ui.time_denominator.currentText())
        self.dodec.repeats = self.ui.no_of_repeats.value()
        self.dodec.voices = self.ui.no_of_voices.value()
        self.dodec.tempo = self.ui.tempo.value()
        self.dodec.notes_value = self.ui.notes_rests_slider.value()
        self.dodec.rests_value = 100 - self.dodec.notes_value
        self.dodec.repeat_current = self.ui.repeat_current_note.isChecked()
        self.dodec.current_chance = self.ui.currentslider.value()
        self.dodec.repeat_previous = self.ui.repeat_previous_note.isChecked()
        self.dodec.previous_chance = self.ui.previousslider.value()
        self.dodec.title = self.ui.score_title.text()
        self.dodec.filename = self.ui.output_filename_2.text()
        self.dodec.foldername = self.ui.output_foldername.text()

    def validate_settings(self):
        """ Validate the provided input settings.
        :return: True if the settings are valid
        :return: False if the settings are not valid """
        # First, make sure that all UI settings are registered.
        self.update_from_ui()

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
