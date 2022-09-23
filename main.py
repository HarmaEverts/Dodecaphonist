from PySide6.QtWidgets import (
    QApplication
    ,QDialog
    ,QMessageBox
    ,QWidget
    ,QLabel
    ,QPushButton
    ,QVBoxLayout
    ,QLineEdit
    ,QComboBox
    ,QRadioButton
)
from PySide6 import QtCore, QtWidgets, QtGui
import sys



app = QApplication(sys.argv)
dialog = QDialog()
dialog.show()
app.exec()