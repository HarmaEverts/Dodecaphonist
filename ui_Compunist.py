# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compunist.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(515, 577)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 9, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.composition_mode = QComboBox(self.groupBox)
        self.composition_mode.setObjectName(u"composition_mode")

        self.gridLayout_2.addWidget(self.composition_mode, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.repeat_current_note = QComboBox(self.groupBox)
        self.repeat_current_note.setObjectName(u"repeat_current_note")

        self.horizontalLayout_3.addWidget(self.repeat_current_note)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.repeat_current_node_chance = QLineEdit(self.groupBox)
        self.repeat_current_node_chance.setObjectName(u"repeat_current_node_chance")

        self.horizontalLayout_3.addWidget(self.repeat_current_node_chance)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 7, 1, 1, 2)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.output_filename = QLineEdit(self.groupBox)
        self.output_filename.setObjectName(u"output_filename")

        self.horizontalLayout.addWidget(self.output_filename)

        self.open_file_explorer = QPushButton(self.groupBox)
        self.open_file_explorer.setObjectName(u"open_file_explorer")

        self.horizontalLayout.addWidget(self.open_file_explorer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 9, 1, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.repeat_previous_note = QComboBox(self.groupBox)
        self.repeat_previous_note.setObjectName(u"repeat_previous_note")

        self.horizontalLayout_2.addWidget(self.repeat_previous_note)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_2.addWidget(self.label_14)

        self.repeat_previous_note_chance = QLineEdit(self.groupBox)
        self.repeat_previous_note_chance.setObjectName(u"repeat_previous_note_chance")

        self.horizontalLayout_2.addWidget(self.repeat_previous_note_chance)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_2.addWidget(self.label_16)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 8, 1, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.notes_rests_slider = QSlider(self.groupBox)
        self.notes_rests_slider.setObjectName(u"notes_rests_slider")
        self.notes_rests_slider.setMaximum(100)
        self.notes_rests_slider.setSliderPosition(100)
        self.notes_rests_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.notes_rests_slider, 0, 1, 1, 1)

        self.percent_rests = QLabel(self.groupBox)
        self.percent_rests.setObjectName(u"percent_rests")

        self.gridLayout.addWidget(self.percent_rests, 0, 3, 1, 1)

        self.percent_notes = QLabel(self.groupBox)
        self.percent_notes.setObjectName(u"percent_notes")

        self.gridLayout.addWidget(self.percent_notes, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 6, 1, 1, 2)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 5, 2, 1, 1)

        self.key = QComboBox(self.groupBox)
        self.key.setObjectName(u"key")

        self.gridLayout_2.addWidget(self.key, 3, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 7, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.tempo = QLineEdit(self.groupBox)
        self.tempo.setObjectName(u"tempo")

        self.gridLayout_2.addWidget(self.tempo, 5, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.time_enumerator = QComboBox(self.groupBox)
        self.time_enumerator.setObjectName(u"time_enumerator")

        self.verticalLayout.addWidget(self.time_enumerator)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.time_denominator = QComboBox(self.groupBox)
        self.time_denominator.setObjectName(u"time_denominator")

        self.verticalLayout.addWidget(self.time_denominator)


        self.gridLayout_2.addLayout(self.verticalLayout, 4, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 4, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 8, 0, 1, 1)

        self.no_of_repeats = QLineEdit(self.groupBox)
        self.no_of_repeats.setObjectName(u"no_of_repeats")

        self.gridLayout_2.addWidget(self.no_of_repeats, 1, 1, 1, 1)

        self.no_of_voices = QSpinBox(self.groupBox)
        self.no_of_voices.setObjectName(u"no_of_voices")

        self.gridLayout_2.addWidget(self.no_of_voices, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.GenerateScore = QPushButton(self.centralwidget)
        self.GenerateScore.setObjectName(u"GenerateScore")

        self.horizontalLayout_5.addWidget(self.GenerateScore)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_7.setBuddy(self.output_filename)
        self.label.setBuddy(self.composition_mode)
        self.label_13.setBuddy(self.repeat_current_node_chance)
        self.label_5.setBuddy(self.tempo)
        self.label_14.setBuddy(self.repeat_previous_note_chance)
        self.label_3.setBuddy(self.no_of_voices)
        self.percent_notes.setBuddy(self.notes_rests_slider)
        self.label_17.setBuddy(self.tempo)
        self.label_2.setBuddy(self.no_of_repeats)
        self.label_12.setBuddy(self.repeat_current_note)
        self.label_4.setBuddy(self.key)
        self.label_11.setBuddy(self.repeat_previous_note)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Compunist", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Compunist score settings", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Output filename", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Compunist mode", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"chance", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tempo", None))
        self.open_file_explorer.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"chance", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Number of voices", None))
        self.percent_rests.setText(QCoreApplication.translate("MainWindow", u"% rests", None))
        self.percent_notes.setText(QCoreApplication.translate("MainWindow", u"% notes", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"bpm", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number of series repeats", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Repeat current note?", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Key signature", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Time signature", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Notes/rests balance", None))
        self.label_18.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Repeat previous note?", None))
        self.GenerateScore.setText(QCoreApplication.translate("MainWindow", u"Generate score", None))
    # retranslateUi

