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
from ui_Compunist import Ui_Compunist


class Compunist(QMainWindow):
    def __init__(self):
        super(Compunist, self).__init__()
        self.ui = Ui_Compunist()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Compunist()
    window.show()
    app.exec()