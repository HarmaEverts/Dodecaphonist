from PySide6.QtWidgets import (
    QApplication
, QMainWindow
)
import sys
from ui_Compunist import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

    def notes_rests_valuechange(self):
        """
        Checks the value of the notes - rests slider, and updates the notes and rests percentage labels accordingly.
        The total should always sum up to 100%
        """
        notes_value = self.ui.notes_rests_slider.value()
        rests_value = 100 - notes_value
        self.ui.percent_notes.setText(str(notes_value) + " % notes")
        self.ui.percent_rests.setText(str(rests_value) + " % rests")

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
