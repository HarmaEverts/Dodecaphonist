# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Compunist.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_Compunist(object):
    def setupUi(self, Compunist):
        if not Compunist.objectName():
            Compunist.setObjectName(u"Compunist")
        Compunist.resize(515, 577)
        self.centralwidget = QWidget(Compunist)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.no_of_voices = QLineEdit(self.groupBox)
        self.no_of_voices.setObjectName(u"no_of_voices")

        self.gridLayout_2.addWidget(self.no_of_voices, 2, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 9, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.mode = QComboBox(self.groupBox)
        self.mode.setObjectName(u"mode")

        self.gridLayout_2.addWidget(self.mode, 0, 1, 1, 1)

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
        self.notes_percentage = QLineEdit(self.groupBox)
        self.notes_percentage.setObjectName(u"notes_percentage")

        self.gridLayout.addWidget(self.notes_percentage, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)

        self.rests_percentage = QLineEdit(self.groupBox)
        self.rests_percentage.setObjectName(u"rests_percentage")

        self.gridLayout.addWidget(self.rests_percentage, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 1, 1, 1)


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

        Compunist.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Compunist)
        self.statusbar.setObjectName(u"statusbar")
        Compunist.setStatusBar(self.statusbar)

        self.retranslateUi(Compunist)

        QMetaObject.connectSlotsByName(Compunist)
    # setupUi

    def retranslateUi(self, Compunist):
        Compunist.setWindowTitle(QCoreApplication.translate("Compunist", u"Compunist", None))
        self.groupBox.setTitle(QCoreApplication.translate("Compunist", u"Compunist score settings", None))
        self.label_7.setText(QCoreApplication.translate("Compunist", u"Output filename", None))
        self.label.setText(QCoreApplication.translate("Compunist", u"Compunist mode", None))
        self.label_13.setText(QCoreApplication.translate("Compunist", u"chance", None))
        self.label_15.setText(QCoreApplication.translate("Compunist", u"%", None))
        self.label_5.setText(QCoreApplication.translate("Compunist", u"Tempo", None))
        self.open_file_explorer.setText(QCoreApplication.translate("Compunist", u"...", None))
        self.label_14.setText(QCoreApplication.translate("Compunist", u"chance", None))
        self.label_16.setText(QCoreApplication.translate("Compunist", u"%", None))
        self.label_3.setText(QCoreApplication.translate("Compunist", u"Number of voices", None))
        self.label_9.setText(QCoreApplication.translate("Compunist", u"% notes", None))
        self.label_10.setText(QCoreApplication.translate("Compunist", u"% rests", None))
        self.label_17.setText(QCoreApplication.translate("Compunist", u"bpm", None))
        self.label_2.setText(QCoreApplication.translate("Compunist", u"Number of series repeats", None))
        self.label_12.setText(QCoreApplication.translate("Compunist", u"Repeat current note?", None))
        self.label_4.setText(QCoreApplication.translate("Compunist", u"Key signature", None))
        self.label_6.setText(QCoreApplication.translate("Compunist", u"Time signature", None))
        self.label_8.setText(QCoreApplication.translate("Compunist", u"Notes/rests balance", None))
        self.label_18.setText("")
        self.label_11.setText(QCoreApplication.translate("Compunist", u"Repeat previous note?", None))
        self.GenerateScore.setText(QCoreApplication.translate("Compunist", u"Generate score", None))
    # retranslateUi

