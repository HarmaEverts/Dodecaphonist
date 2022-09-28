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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(515, 597)
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
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 10, 2, 1, 1)

        self.output_filename_2 = QLineEdit(self.groupBox)
        self.output_filename_2.setObjectName(u"output_filename_2")

        self.gridLayout_2.addWidget(self.output_filename_2, 16, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.repeat_previous_note = QCheckBox(self.groupBox)
        self.repeat_previous_note.setObjectName(u"repeat_previous_note")

        self.horizontalLayout_2.addWidget(self.repeat_previous_note)

        self.previouslabel = QLabel(self.groupBox)
        self.previouslabel.setObjectName(u"previouslabel")
        self.previouslabel.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.previouslabel)

        self.previousslider = QSlider(self.groupBox)
        self.previousslider.setObjectName(u"previousslider")
        self.previousslider.setEnabled(False)
        self.previousslider.setMinimum(1)
        self.previousslider.setMaximum(100)
        self.previousslider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.previousslider)

        self.previouspercentage = QLabel(self.groupBox)
        self.previouspercentage.setObjectName(u"previouspercentage")
        self.previouspercentage.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.previouspercentage)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 14, 1, 1, 2)

        self.score_title = QLineEdit(self.groupBox)
        self.score_title.setObjectName(u"score_title")

        self.gridLayout_2.addWidget(self.score_title, 15, 1, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.repeat_current_note = QCheckBox(self.groupBox)
        self.repeat_current_note.setObjectName(u"repeat_current_note")

        self.horizontalLayout_3.addWidget(self.repeat_current_note)

        self.currentlabel = QLabel(self.groupBox)
        self.currentlabel.setObjectName(u"currentlabel")
        self.currentlabel.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.currentlabel)

        self.currentslider = QSlider(self.groupBox)
        self.currentslider.setObjectName(u"currentslider")
        self.currentslider.setEnabled(False)
        self.currentslider.setMinimum(1)
        self.currentslider.setMaximum(100)
        self.currentslider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.currentslider)

        self.currentpercentage = QLabel(self.groupBox)
        self.currentpercentage.setObjectName(u"currentpercentage")
        self.currentpercentage.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.currentpercentage)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 13, 1, 1, 2)

        self.composition_mode = QComboBox(self.groupBox)
        self.composition_mode.setObjectName(u"composition_mode")

        self.gridLayout_2.addWidget(self.composition_mode, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.output_foldername = QLineEdit(self.groupBox)
        self.output_foldername.setObjectName(u"output_foldername")

        self.horizontalLayout.addWidget(self.output_foldername)

        self.open_file_explorer = QPushButton(self.groupBox)
        self.open_file_explorer.setObjectName(u"open_file_explorer")

        self.horizontalLayout.addWidget(self.open_file_explorer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 17, 1, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.notes_rests_slider = QSlider(self.groupBox)
        self.notes_rests_slider.setObjectName(u"notes_rests_slider")
        self.notes_rests_slider.setMaximum(100)
        self.notes_rests_slider.setSliderPosition(100)
        self.notes_rests_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.notes_rests_slider, 0, 1, 1, 1)

        self.percent_notes = QLabel(self.groupBox)
        self.percent_notes.setObjectName(u"percent_notes")

        self.gridLayout.addWidget(self.percent_notes, 0, 0, 1, 1)

        self.percent_rests = QLabel(self.groupBox)
        self.percent_rests.setObjectName(u"percent_rests")

        self.gridLayout.addWidget(self.percent_rests, 0, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 12, 1, 1, 2)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 11, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 10, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 13, 0, 1, 1)

        self.key = QComboBox(self.groupBox)
        self.key.setObjectName(u"key")

        self.gridLayout_2.addWidget(self.key, 9, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 11, 0, 1, 1)

        self.no_of_repeats = QSpinBox(self.groupBox)
        self.no_of_repeats.setObjectName(u"no_of_repeats")
        self.no_of_repeats.setMinimum(1)
        self.no_of_repeats.setValue(10)

        self.gridLayout_2.addWidget(self.no_of_repeats, 1, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 15, 0, 1, 1)

        self.tempo = QSpinBox(self.groupBox)
        self.tempo.setObjectName(u"tempo")
        self.tempo.setMinimum(12)
        self.tempo.setMaximum(200)
        self.tempo.setValue(60)

        self.gridLayout_2.addWidget(self.tempo, 11, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 16, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 16, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.time_enumerator = QComboBox(self.groupBox)
        self.time_enumerator.setObjectName(u"time_enumerator")
        self.time_enumerator.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.time_enumerator)

        self.time_denominator = QComboBox(self.groupBox)
        self.time_denominator.setObjectName(u"time_denominator")
        self.time_denominator.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.time_denominator)


        self.gridLayout_2.addLayout(self.verticalLayout, 10, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 14, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 17, 0, 1, 1)

        self.no_of_voices = QSpinBox(self.groupBox)
        self.no_of_voices.setObjectName(u"no_of_voices")
        self.no_of_voices.setMinimum(1)
        self.no_of_voices.setMaximum(6)

        self.gridLayout_2.addWidget(self.no_of_voices, 2, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 12, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 9, 0, 1, 1)

        self.voice1label = QLabel(self.groupBox)
        self.voice1label.setObjectName(u"voice1label")
        self.voice1label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.voice1label, 3, 0, 1, 1)

        self.voice2label = QLabel(self.groupBox)
        self.voice2label.setObjectName(u"voice2label")
        self.voice2label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.voice2label, 4, 0, 1, 1)

        self.voice3label = QLabel(self.groupBox)
        self.voice3label.setObjectName(u"voice3label")
        self.voice3label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.voice3label, 5, 0, 1, 1)

        self.voice4label = QLabel(self.groupBox)
        self.voice4label.setObjectName(u"voice4label")
        self.voice4label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.voice4label, 6, 0, 1, 1)

        self.voice5label = QLabel(self.groupBox)
        self.voice5label.setObjectName(u"voice5label")
        self.voice5label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.voice5label, 7, 0, 1, 1)

        self.voice6label = QLabel(self.groupBox)
        self.voice6label.setObjectName(u"voice6label")
        self.voice6label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.voice6label, 8, 0, 1, 1)

        self.voice1 = QComboBox(self.groupBox)
        self.voice1.setObjectName(u"voice1")

        self.gridLayout_2.addWidget(self.voice1, 3, 1, 1, 1)

        self.voice2 = QComboBox(self.groupBox)
        self.voice2.setObjectName(u"voice2")

        self.gridLayout_2.addWidget(self.voice2, 4, 1, 1, 1)

        self.voice3 = QComboBox(self.groupBox)
        self.voice3.setObjectName(u"voice3")

        self.gridLayout_2.addWidget(self.voice3, 5, 1, 1, 1)

        self.voice4 = QComboBox(self.groupBox)
        self.voice4.setObjectName(u"voice4")

        self.gridLayout_2.addWidget(self.voice4, 6, 1, 1, 1)

        self.voice5 = QComboBox(self.groupBox)
        self.voice5.setObjectName(u"voice5")

        self.gridLayout_2.addWidget(self.voice5, 7, 1, 1, 1)

        self.voice6 = QComboBox(self.groupBox)
        self.voice6.setObjectName(u"voice6")

        self.gridLayout_2.addWidget(self.voice6, 8, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.generate_score = QPushButton(self.centralwidget)
        self.generate_score.setObjectName(u"generate_score")

        self.horizontalLayout_5.addWidget(self.generate_score)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.no_of_voices)
        self.percent_notes.setBuddy(self.notes_rests_slider)
        self.label.setBuddy(self.composition_mode)
        self.label_7.setBuddy(self.output_foldername)
        self.label_4.setBuddy(self.key)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.composition_mode, self.no_of_repeats)
        QWidget.setTabOrder(self.no_of_repeats, self.no_of_voices)
        QWidget.setTabOrder(self.no_of_voices, self.key)
        QWidget.setTabOrder(self.key, self.time_enumerator)
        QWidget.setTabOrder(self.time_enumerator, self.time_denominator)
        QWidget.setTabOrder(self.time_denominator, self.tempo)
        QWidget.setTabOrder(self.tempo, self.notes_rests_slider)
        QWidget.setTabOrder(self.notes_rests_slider, self.repeat_current_note)
        QWidget.setTabOrder(self.repeat_current_note, self.currentslider)
        QWidget.setTabOrder(self.currentslider, self.repeat_previous_note)
        QWidget.setTabOrder(self.repeat_previous_note, self.previousslider)
        QWidget.setTabOrder(self.previousslider, self.score_title)
        QWidget.setTabOrder(self.score_title, self.output_filename_2)
        QWidget.setTabOrder(self.output_filename_2, self.output_foldername)
        QWidget.setTabOrder(self.output_foldername, self.open_file_explorer)
        QWidget.setTabOrder(self.open_file_explorer, self.generate_score)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Compunist", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Compunist score settings", None))
        self.label_18.setText("")
        self.repeat_previous_note.setText("")
        self.previouslabel.setText(QCoreApplication.translate("MainWindow", u"    Chance", None))
        self.previouspercentage.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.repeat_current_note.setText("")
        self.currentlabel.setText(QCoreApplication.translate("MainWindow", u"    Chance", None))
        self.currentpercentage.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Number of voices", None))
        self.open_file_explorer.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.percent_notes.setText(QCoreApplication.translate("MainWindow", u"100 % notes", None))
        self.percent_rests.setText(QCoreApplication.translate("MainWindow", u"0 % rests", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"bpm", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Time signature", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Template", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Repeat current note", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tempo", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Score title", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u".pdf", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Output filename", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Repeat previous note", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number of series repeats", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Output folder", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Notes/rests balance", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Key signature", None))
        self.voice1label.setText(QCoreApplication.translate("MainWindow", u"Voice 1", None))
        self.voice2label.setText(QCoreApplication.translate("MainWindow", u"Voice 2", None))
        self.voice3label.setText(QCoreApplication.translate("MainWindow", u"Voice 3", None))
        self.voice4label.setText(QCoreApplication.translate("MainWindow", u"Voice 4", None))
        self.voice5label.setText(QCoreApplication.translate("MainWindow", u"Voice 5", None))
        self.voice6label.setText(QCoreApplication.translate("MainWindow", u"Voice 6", None))
        self.generate_score.setText(QCoreApplication.translate("MainWindow", u"Generate score", None))
    # retranslateUi

