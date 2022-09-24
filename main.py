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

        self.ui.composition_mode.addItems(["Schoenberg", "Webern", "Stravinsky", "Custom"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()