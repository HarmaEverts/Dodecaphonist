from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QApplication
, QMainWindow, QFileDialog
)
import sys
from ui_Compunist import Ui_MainWindow
from compusition import Compusition


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.comp = Compusition()
        self.comp.filename = ""
        self.comp.foldername = ""
        self.comp.title = ""

        # Set up the UI options in drop-downs etc.
        self.ui.composition_mode.addItems(["Schoenberg", "Webern", "Stravinsky", "Start from scratch"])
        self.ui.key.addItems(["Sharps", "Flats"])
        enumerator_options = range(1, 13)
        denominator_options = [1, 2, 4, 8, 16, 32]
        self.ui.time_enumerator.addItems([str(x) for x in enumerator_options])
        self.ui.time_denominator.addItems([str(x) for x in denominator_options])

        self.ui.notes_rests_slider.valueChanged.connect(self.notes_rests_valuechange)
        self.ui.repeat_current_note.stateChanged.connect(self.toggle_repeat_current_note)
        self.ui.repeat_previous_note.stateChanged.connect(self.toggle_repeat_previous_note)

        self.ui.open_file_explorer.clicked.connect(self.browse_folder)

        self.ui.generate_score.clicked.connect(self.create_score)

    def notes_rests_valuechange(self):
        """
        Checks the value of the notes - rests slider, and updates the notes and rests percentage labels accordingly.
        The total should always sum up to 100%
        """
        self.comp.notes_value = self.ui.notes_rests_slider.value()
        self.comp.rests_value = 100 - self.comp.notes_value
        self.ui.percent_notes.setText(str(self.comp.notes_value) + " % notes")
        self.ui.percent_rests.setText(str(self.comp.rests_value) + " % rests")

    def toggle_repeat_current_note(self):
        """
        Toggles the repeat current note details depending on whether the checkbox is selected.
        """
        self.ui.currentlabel.setEnabled(self.ui.repeat_current_note.isChecked())
        self.ui.currentslider.setEnabled(self.ui.repeat_current_note.isChecked())
        self.ui.currentpercentage.setEnabled(self.ui.repeat_current_note.isChecked())

    def toggle_repeat_previous_note(self):
        """
        Toggles the repeat previous note details depending on whether the checkbox is selected.
        """
        self.ui.previouslabel.setEnabled(self.ui.repeat_previous_note.isChecked())
        self.ui.previousslider.setEnabled(self.ui.repeat_previous_note.isChecked())
        self.ui.previouspercentage.setEnabled(self.ui.repeat_previous_note.isChecked())

    def browse_folder(self):
        """
        Selects the folder in which the generated files will be saved.
        """
        self.comp.foldername = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.output_foldername.setText(self.comp.foldername)

    def check_input(self):
        """
        Validate the provided input settings.
        :return: True if the settings are valid
        :return: False if the settings are not valid
        """
        return True

    def create_score(self):
        """
        Creates a Compusition object based on the provided settings and outputs the generated compusition (.ly)
        to the specified folder with the filename as its name.
        """
        if self.check_input():
            self.comp.generate()
        else:
            print("Invalid settings.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
