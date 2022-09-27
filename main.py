from PySide6.QtWidgets import (
    QApplication
, QDialog
, QMessageBox
, QWidget
, QLabel
, QPushButton
, QVBoxLayout
, QLineEdit
, QComboBox
, QRadioButton
, QMainWindow
)
from PySide6 import QtCore, QtWidgets, QtGui
import sys
from ui_Compunist import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up the UI options in drop-downs etc.
        self.ui.composition_mode.addItems(["Schoenberg", "Webern", "Stravinsky", "Custom"])
        self.ui.key.addItems(["Sharps", "Flats"])
        self.ui.repeat_current_note.addItems(["Yes", "No"])
        self.ui.repeat_previous_note.addItems(["Yes", "No"])
        enumerator_options = range(1, 13)
        denominator_options = [1, 2, 4, 8, 16, 32]
        self.ui.time_enumerator.addItems([str(x) for x in enumerator_options])
        self.ui.time_denominator.addItems([str(x) for x in denominator_options])

        self.ui.notes_rests_slider.valueChanged.connect(self.valuechange)

    def valuechange(self):
        """
        Checks the value of the notes - rests slider, and updates the notes and rests percentage labels accordingly.
        The total should always sum up to 100%
        """
        notes_value = self.ui.notes_rests_slider.value()
        rests_value = 100 - notes_value
        self.ui.percent_notes.setText(str(notes_value) + " % notes")
        self.ui.percent_rests.setText(str(rests_value) + " % rests")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()