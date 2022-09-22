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
import sys



app = QApplication(sys.argv)
dialog = QDialog()
dialog.show()
app.exec()