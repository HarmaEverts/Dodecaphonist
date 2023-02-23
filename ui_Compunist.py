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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1239, 746)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.time_enumerator = QComboBox(self.groupBox_4)
        self.time_enumerator.setObjectName(u"time_enumerator")
        self.time_enumerator.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.time_enumerator)

        self.time_denominator = QComboBox(self.groupBox_4)
        self.time_denominator.setObjectName(u"time_denominator")
        self.time_denominator.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.time_denominator)


        self.gridLayout_5.addLayout(self.verticalLayout, 3, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.notes_rests_slider = QSlider(self.groupBox_4)
        self.notes_rests_slider.setObjectName(u"notes_rests_slider")
        self.notes_rests_slider.setMaximum(100)
        self.notes_rests_slider.setSliderPosition(100)
        self.notes_rests_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.notes_rests_slider, 0, 1, 1, 1)

        self.percent_rests = QLabel(self.groupBox_4)
        self.percent_rests.setObjectName(u"percent_rests")

        self.gridLayout.addWidget(self.percent_rests, 0, 3, 1, 1)

        self.percent_notes = QLabel(self.groupBox_4)
        self.percent_notes.setObjectName(u"percent_notes")

        self.gridLayout.addWidget(self.percent_notes, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 6, 1, 1, 2)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 7, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 6, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 4, 0, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.tempo = QSpinBox(self.groupBox_4)
        self.tempo.setObjectName(u"tempo")
        self.tempo.setMinimum(12)
        self.tempo.setMaximum(200)
        self.tempo.setValue(60)

        self.gridLayout_5.addWidget(self.tempo, 4, 1, 1, 1)

        self.key = QComboBox(self.groupBox_4)
        self.key.setObjectName(u"key")

        self.gridLayout_5.addWidget(self.key, 1, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 4, 2, 1, 1)

        self.no_of_repeats = QSpinBox(self.groupBox_4)
        self.no_of_repeats.setObjectName(u"no_of_repeats")
        self.no_of_repeats.setMinimum(1)
        self.no_of_repeats.setValue(10)

        self.gridLayout_5.addWidget(self.no_of_repeats, 5, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 5, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 8, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.currentslider = QSlider(self.groupBox_4)
        self.currentslider.setObjectName(u"currentslider")
        self.currentslider.setEnabled(False)
        self.currentslider.setMinimum(0)
        self.currentslider.setMaximum(99)
        self.currentslider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.currentslider)

        self.currentpercentage = QLabel(self.groupBox_4)
        self.currentpercentage.setObjectName(u"currentpercentage")
        self.currentpercentage.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.currentpercentage)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 7, 1, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.previousslider = QSlider(self.groupBox_4)
        self.previousslider.setObjectName(u"previousslider")
        self.previousslider.setEnabled(False)
        self.previousslider.setMinimum(0)
        self.previousslider.setMaximum(99)
        self.previousslider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.previousslider)

        self.previouspercentage = QLabel(self.groupBox_4)
        self.previouspercentage.setObjectName(u"previouspercentage")
        self.previouspercentage.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.previouspercentage)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 8, 1, 1, 2)

        self.composition_mode = QComboBox(self.groupBox_4)
        self.composition_mode.setObjectName(u"composition_mode")

        self.gridLayout_5.addWidget(self.composition_mode, 0, 1, 1, 2)


        self.gridLayout_6.addWidget(self.groupBox_4, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.v1 = QWidget(self.groupBox_2)
        self.v1.setObjectName(u"v1")
        self.horizontalLayout_6 = QHBoxLayout(self.v1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.voice1label = QLabel(self.v1)
        self.voice1label.setObjectName(u"voice1label")
        self.voice1label.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.voice1label)

        self.voice1 = QComboBox(self.v1)
        self.voice1.setObjectName(u"voice1")

        self.horizontalLayout_6.addWidget(self.voice1)


        self.verticalLayout_2.addWidget(self.v1)

        self.v2 = QWidget(self.groupBox_2)
        self.v2.setObjectName(u"v2")
        self.horizontalLayout_7 = QHBoxLayout(self.v2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.voice2label = QLabel(self.v2)
        self.voice2label.setObjectName(u"voice2label")
        self.voice2label.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.voice2label)

        self.voice2 = QComboBox(self.v2)
        self.voice2.setObjectName(u"voice2")

        self.horizontalLayout_7.addWidget(self.voice2)


        self.verticalLayout_2.addWidget(self.v2)

        self.v3_2 = QWidget(self.groupBox_2)
        self.v3_2.setObjectName(u"v3_2")
        self.v3 = QHBoxLayout(self.v3_2)
        self.v3.setObjectName(u"v3")
        self.voice3label = QLabel(self.v3_2)
        self.voice3label.setObjectName(u"voice3label")
        self.voice3label.setStyleSheet(u"")

        self.v3.addWidget(self.voice3label)

        self.voice3 = QComboBox(self.v3_2)
        self.voice3.setObjectName(u"voice3")

        self.v3.addWidget(self.voice3)


        self.verticalLayout_2.addWidget(self.v3_2)

        self.v4_2 = QWidget(self.groupBox_2)
        self.v4_2.setObjectName(u"v4_2")
        self.v4 = QHBoxLayout(self.v4_2)
        self.v4.setObjectName(u"v4")
        self.voice4label = QLabel(self.v4_2)
        self.voice4label.setObjectName(u"voice4label")
        self.voice4label.setStyleSheet(u"")

        self.v4.addWidget(self.voice4label)

        self.voice4 = QComboBox(self.v4_2)
        self.voice4.setObjectName(u"voice4")

        self.v4.addWidget(self.voice4)


        self.verticalLayout_2.addWidget(self.v4_2)

        self.v5_2 = QWidget(self.groupBox_2)
        self.v5_2.setObjectName(u"v5_2")
        self.v5 = QHBoxLayout(self.v5_2)
        self.v5.setObjectName(u"v5")
        self.voice5label = QLabel(self.v5_2)
        self.voice5label.setObjectName(u"voice5label")
        self.voice5label.setStyleSheet(u"")

        self.v5.addWidget(self.voice5label)

        self.voice5 = QComboBox(self.v5_2)
        self.voice5.setObjectName(u"voice5")

        self.v5.addWidget(self.voice5)


        self.verticalLayout_2.addWidget(self.v5_2)

        self.v6_2 = QWidget(self.groupBox_2)
        self.v6_2.setObjectName(u"v6_2")
        self.v6 = QHBoxLayout(self.v6_2)
        self.v6.setObjectName(u"v6")
        self.voice6label = QLabel(self.v6_2)
        self.voice6label.setObjectName(u"voice6label")
        self.voice6label.setStyleSheet(u"")

        self.v6.addWidget(self.voice6label)

        self.voice6 = QComboBox(self.v6_2)
        self.voice6.setObjectName(u"voice6")

        self.v6.addWidget(self.voice6)


        self.verticalLayout_2.addWidget(self.v6_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 2)


        self.gridLayout_6.addWidget(self.groupBox_2, 0, 2, 1, 1)

        self.groupBox_8 = QGroupBox(self.groupBox)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_10 = QGridLayout(self.groupBox_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.series_label = QLabel(self.groupBox_8)
        self.series_label.setObjectName(u"series_label")

        self.gridLayout_10.addWidget(self.series_label, 1, 0, 1, 1)

        self.generate_series = QPushButton(self.groupBox_8)
        self.generate_series.setObjectName(u"generate_series")

        self.gridLayout_10.addWidget(self.generate_series, 0, 0, 1, 1)

        self.series_preview = QLineEdit(self.groupBox_8)
        self.series_preview.setObjectName(u"series_preview")

        self.gridLayout_10.addWidget(self.series_preview, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_8, 1, 0, 1, 3)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_8 = QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.dotted_half_note_slider = QSlider(self.groupBox_5)
        self.dotted_half_note_slider.setObjectName(u"dotted_half_note_slider")
        self.dotted_half_note_slider.setMaximum(100)
        self.dotted_half_note_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.dotted_half_note_slider, 3, 1, 1, 1)

        self.dotted_eighth_note_pc = QLabel(self.groupBox_5)
        self.dotted_eighth_note_pc.setObjectName(u"dotted_eighth_note_pc")

        self.gridLayout_8.addWidget(self.dotted_eighth_note_pc, 7, 2, 1, 1)

        self.eighth_note_pc = QLabel(self.groupBox_5)
        self.eighth_note_pc.setObjectName(u"eighth_note_pc")

        self.gridLayout_8.addWidget(self.eighth_note_pc, 6, 2, 1, 1)

        self.dotted_whole_note_pc = QLabel(self.groupBox_5)
        self.dotted_whole_note_pc.setObjectName(u"dotted_whole_note_pc")

        self.gridLayout_8.addWidget(self.dotted_whole_note_pc, 1, 2, 1, 1)

        self.dotted_whole_note_slider = QSlider(self.groupBox_5)
        self.dotted_whole_note_slider.setObjectName(u"dotted_whole_note_slider")
        self.dotted_whole_note_slider.setMaximum(100)
        self.dotted_whole_note_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.dotted_whole_note_slider, 1, 1, 1, 1)

        self.dotted_quarter_note = QLabel(self.groupBox_5)
        self.dotted_quarter_note.setObjectName(u"dotted_quarter_note")
        self.dotted_quarter_note.setPixmap(QPixmap(u":/icons/dotted quarter note"))
        self.dotted_quarter_note.setScaledContents(True)

        self.gridLayout_8.addWidget(self.dotted_quarter_note, 5, 0, 1, 1)

        self.dotted_eighth_note_slider = QSlider(self.groupBox_5)
        self.dotted_eighth_note_slider.setObjectName(u"dotted_eighth_note_slider")
        self.dotted_eighth_note_slider.setMaximum(100)
        self.dotted_eighth_note_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.dotted_eighth_note_slider, 7, 1, 1, 1)

        self.dotted_quarter_note_pc = QLabel(self.groupBox_5)
        self.dotted_quarter_note_pc.setObjectName(u"dotted_quarter_note_pc")

        self.gridLayout_8.addWidget(self.dotted_quarter_note_pc, 5, 2, 1, 1)

        self.quarter_note_pc = QLabel(self.groupBox_5)
        self.quarter_note_pc.setObjectName(u"quarter_note_pc")

        self.gridLayout_8.addWidget(self.quarter_note_pc, 4, 2, 1, 1)

        self.dotted_whole_note = QLabel(self.groupBox_5)
        self.dotted_whole_note.setObjectName(u"dotted_whole_note")
        self.dotted_whole_note.setPixmap(QPixmap(u":/icons/dotted whole note"))
        self.dotted_whole_note.setScaledContents(True)

        self.gridLayout_8.addWidget(self.dotted_whole_note, 1, 0, 1, 1)

        self.whole_note_pc = QLabel(self.groupBox_5)
        self.whole_note_pc.setObjectName(u"whole_note_pc")
        self.whole_note_pc.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.whole_note_pc, 0, 2, 1, 1)

        self.dotted_half_note = QLabel(self.groupBox_5)
        self.dotted_half_note.setObjectName(u"dotted_half_note")
        self.dotted_half_note.setPixmap(QPixmap(u":/icons/dotted half note"))
        self.dotted_half_note.setScaledContents(True)

        self.gridLayout_8.addWidget(self.dotted_half_note, 3, 0, 1, 1)

        self.eighth_note_slider = QSlider(self.groupBox_5)
        self.eighth_note_slider.setObjectName(u"eighth_note_slider")
        self.eighth_note_slider.setMaximum(100)
        self.eighth_note_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.eighth_note_slider, 6, 1, 1, 1)

        self.sixteenth_note_slider = QSlider(self.groupBox_5)
        self.sixteenth_note_slider.setObjectName(u"sixteenth_note_slider")
        self.sixteenth_note_slider.setMaximum(100)
        self.sixteenth_note_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.sixteenth_note_slider, 8, 1, 1, 1)

        self.dotted_quarter_note_slider = QSlider(self.groupBox_5)
        self.dotted_quarter_note_slider.setObjectName(u"dotted_quarter_note_slider")
        self.dotted_quarter_note_slider.setMaximum(100)
        self.dotted_quarter_note_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.dotted_quarter_note_slider, 5, 1, 1, 1)

        self.dotted_half_note_pc = QLabel(self.groupBox_5)
        self.dotted_half_note_pc.setObjectName(u"dotted_half_note_pc")

        self.gridLayout_8.addWidget(self.dotted_half_note_pc, 3, 2, 1, 1)

        self.whole_note_slider = QSlider(self.groupBox_5)
        self.whole_note_slider.setObjectName(u"whole_note_slider")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whole_note_slider.sizePolicy().hasHeightForWidth())
        self.whole_note_slider.setSizePolicy(sizePolicy)
        self.whole_note_slider.setMaximum(100)
        self.whole_note_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.whole_note_slider, 0, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u":/icons/eighth note"))
        self.label_19.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_19, 6, 0, 1, 1)

        self.half_note_pc = QLabel(self.groupBox_5)
        self.half_note_pc.setObjectName(u"half_note_pc")

        self.gridLayout_8.addWidget(self.half_note_pc, 2, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"")
        self.label_15.setPixmap(QPixmap(u":/icons/half note"))
        self.label_15.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_15, 2, 0, 1, 1)

        self.dotted_eighth_note = QLabel(self.groupBox_5)
        self.dotted_eighth_note.setObjectName(u"dotted_eighth_note")
        self.dotted_eighth_note.setPixmap(QPixmap(u":/icons/dotted eighth note"))
        self.dotted_eighth_note.setScaledContents(True)

        self.gridLayout_8.addWidget(self.dotted_eighth_note, 7, 0, 1, 1)

        self.half_note_slider = QSlider(self.groupBox_5)
        self.half_note_slider.setObjectName(u"half_note_slider")
        self.half_note_slider.setMaximum(100)
        self.half_note_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.half_note_slider, 2, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setPixmap(QPixmap(u":/icons/quarter note"))
        self.label_16.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_16, 4, 0, 1, 1)

        self.sixteenth_note_pc = QLabel(self.groupBox_5)
        self.sixteenth_note_pc.setObjectName(u"sixteenth_note_pc")

        self.gridLayout_8.addWidget(self.sixteenth_note_pc, 8, 2, 1, 1)

        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setPixmap(QPixmap(u":/icons/sixteenth note"))
        self.label_20.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_20, 8, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/icons/whole note"))
        self.label_14.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_14, 0, 0, 1, 1)

        self.quarter_note_slider = QSlider(self.groupBox_5)
        self.quarter_note_slider.setObjectName(u"quarter_note_slider")
        self.quarter_note_slider.setMaximum(100)
        self.quarter_note_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.quarter_note_slider, 4, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_5, 0, 3, 3, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.output_foldername = QLineEdit(self.groupBox_3)
        self.output_foldername.setObjectName(u"output_foldername")

        self.horizontalLayout.addWidget(self.output_foldername)

        self.open_file_explorer = QPushButton(self.groupBox_3)
        self.open_file_explorer.setObjectName(u"open_file_explorer")

        self.horizontalLayout.addWidget(self.open_file_explorer)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)

        self.output_filename_2 = QLineEdit(self.groupBox_3)
        self.output_filename_2.setObjectName(u"output_filename_2")

        self.gridLayout_3.addWidget(self.output_filename_2, 1, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 1, 1, 1, 1)

        self.score_title = QLineEdit(self.groupBox_3)
        self.score_title.setObjectName(u"score_title")

        self.gridLayout_3.addWidget(self.score_title, 0, 2, 1, 1)

        self.generate_score = QPushButton(self.groupBox_3)
        self.generate_score.setObjectName(u"generate_score")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generate_score.sizePolicy().hasHeightForWidth())
        self.generate_score.setSizePolicy(sizePolicy1)
        self.generate_score.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.generate_score, 3, 2, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_3, 2, 0, 1, 3)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_9 = QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.dotted_quarter_rest_slider = QSlider(self.groupBox_7)
        self.dotted_quarter_rest_slider.setObjectName(u"dotted_quarter_rest_slider")
        self.dotted_quarter_rest_slider.setMaximum(100)
        self.dotted_quarter_rest_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.dotted_quarter_rest_slider, 5, 1, 1, 1)

        self.sixteenth_rest_pc = QLabel(self.groupBox_7)
        self.sixteenth_rest_pc.setObjectName(u"sixteenth_rest_pc")

        self.gridLayout_9.addWidget(self.sixteenth_rest_pc, 8, 2, 1, 1)

        self.dotted_quarter_rest_pc = QLabel(self.groupBox_7)
        self.dotted_quarter_rest_pc.setObjectName(u"dotted_quarter_rest_pc")

        self.gridLayout_9.addWidget(self.dotted_quarter_rest_pc, 5, 2, 1, 1)

        self.dotted_half_rest = QLabel(self.groupBox_7)
        self.dotted_half_rest.setObjectName(u"dotted_half_rest")
        self.dotted_half_rest.setPixmap(QPixmap(u":/icons/dotted half rest"))
        self.dotted_half_rest.setScaledContents(True)

        self.gridLayout_9.addWidget(self.dotted_half_rest, 3, 0, 1, 1)

        self.sixteenth_rest_slider = QSlider(self.groupBox_7)
        self.sixteenth_rest_slider.setObjectName(u"sixteenth_rest_slider")
        self.sixteenth_rest_slider.setMaximum(100)
        self.sixteenth_rest_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.sixteenth_rest_slider, 8, 1, 1, 1)

        self.whole_rest_slider = QSlider(self.groupBox_7)
        self.whole_rest_slider.setObjectName(u"whole_rest_slider")
        self.whole_rest_slider.setMaximum(100)
        self.whole_rest_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.whole_rest_slider, 0, 1, 1, 1)

        self.quarter_rest_pc = QLabel(self.groupBox_7)
        self.quarter_rest_pc.setObjectName(u"quarter_rest_pc")

        self.gridLayout_9.addWidget(self.quarter_rest_pc, 4, 2, 1, 1)

        self.eighth_rest_pc = QLabel(self.groupBox_7)
        self.eighth_rest_pc.setObjectName(u"eighth_rest_pc")

        self.gridLayout_9.addWidget(self.eighth_rest_pc, 6, 2, 1, 1)

        self.quarter_rest_slider = QSlider(self.groupBox_7)
        self.quarter_rest_slider.setObjectName(u"quarter_rest_slider")
        self.quarter_rest_slider.setMaximum(100)
        self.quarter_rest_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.quarter_rest_slider, 4, 1, 1, 1)

        self.dotted_whole_rest_pc = QLabel(self.groupBox_7)
        self.dotted_whole_rest_pc.setObjectName(u"dotted_whole_rest_pc")

        self.gridLayout_9.addWidget(self.dotted_whole_rest_pc, 1, 2, 1, 1)

        self.label_23 = QLabel(self.groupBox_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setPixmap(QPixmap(u":/icons/half rest"))
        self.label_23.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label_23, 2, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setPixmap(QPixmap(u":/icons/eighth rest"))
        self.label_25.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label_25, 6, 0, 1, 1)

        self.dotted_whole_rest = QLabel(self.groupBox_7)
        self.dotted_whole_rest.setObjectName(u"dotted_whole_rest")
        self.dotted_whole_rest.setPixmap(QPixmap(u":/icons/dotted whole rest"))
        self.dotted_whole_rest.setScaledContents(True)

        self.gridLayout_9.addWidget(self.dotted_whole_rest, 1, 0, 1, 1)

        self.half_rest_slider = QSlider(self.groupBox_7)
        self.half_rest_slider.setObjectName(u"half_rest_slider")
        self.half_rest_slider.setMaximum(100)
        self.half_rest_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.half_rest_slider, 2, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setPixmap(QPixmap(u":/icons/whole rest"))
        self.label_22.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label_22, 0, 0, 1, 1)

        self.dotted_quarter_rest = QLabel(self.groupBox_7)
        self.dotted_quarter_rest.setObjectName(u"dotted_quarter_rest")
        self.dotted_quarter_rest.setPixmap(QPixmap(u":/icons/dotted quarter rest"))
        self.dotted_quarter_rest.setScaledContents(True)

        self.gridLayout_9.addWidget(self.dotted_quarter_rest, 5, 0, 1, 1)

        self.eighth_rest_slider = QSlider(self.groupBox_7)
        self.eighth_rest_slider.setObjectName(u"eighth_rest_slider")
        self.eighth_rest_slider.setMaximum(100)
        self.eighth_rest_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.eighth_rest_slider, 6, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setPixmap(QPixmap(u":/icons/quarter rest"))
        self.label_24.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label_24, 4, 0, 1, 1)

        self.whole_rest_pc = QLabel(self.groupBox_7)
        self.whole_rest_pc.setObjectName(u"whole_rest_pc")

        self.gridLayout_9.addWidget(self.whole_rest_pc, 0, 2, 1, 1)

        self.dotted_whole_rest_slider = QSlider(self.groupBox_7)
        self.dotted_whole_rest_slider.setObjectName(u"dotted_whole_rest_slider")
        self.dotted_whole_rest_slider.setMaximum(100)
        self.dotted_whole_rest_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.dotted_whole_rest_slider, 1, 1, 1, 1)

        self.half_rest_pc = QLabel(self.groupBox_7)
        self.half_rest_pc.setObjectName(u"half_rest_pc")

        self.gridLayout_9.addWidget(self.half_rest_pc, 2, 2, 1, 1)

        self.label_26 = QLabel(self.groupBox_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setPixmap(QPixmap(u":/icons/sixteenth rest"))
        self.label_26.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label_26, 8, 0, 1, 1)

        self.dotted_half_rest_slider = QSlider(self.groupBox_7)
        self.dotted_half_rest_slider.setObjectName(u"dotted_half_rest_slider")
        self.dotted_half_rest_slider.setMaximum(100)
        self.dotted_half_rest_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.dotted_half_rest_slider, 3, 1, 1, 1)

        self.dotted_half_rest_pc = QLabel(self.groupBox_7)
        self.dotted_half_rest_pc.setObjectName(u"dotted_half_rest_pc")

        self.gridLayout_9.addWidget(self.dotted_half_rest_pc, 3, 2, 1, 1)

        self.dotted_eighth_rest = QLabel(self.groupBox_7)
        self.dotted_eighth_rest.setObjectName(u"dotted_eighth_rest")
        self.dotted_eighth_rest.setPixmap(QPixmap(u":/icons/dotted eighth rest"))
        self.dotted_eighth_rest.setScaledContents(True)

        self.gridLayout_9.addWidget(self.dotted_eighth_rest, 7, 0, 1, 1)

        self.dotted_eighth_rest_slider = QSlider(self.groupBox_7)
        self.dotted_eighth_rest_slider.setObjectName(u"dotted_eighth_rest_slider")
        self.dotted_eighth_rest_slider.setMaximum(100)
        self.dotted_eighth_rest_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.dotted_eighth_rest_slider, 7, 1, 1, 1)

        self.dotted_eighth_rest_labe = QLabel(self.groupBox_7)
        self.dotted_eighth_rest_labe.setObjectName(u"dotted_eighth_rest_labe")

        self.gridLayout_9.addWidget(self.dotted_eighth_rest_labe, 7, 2, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_7, 0, 4, 3, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_4.setBuddy(self.key)
        self.percent_notes.setBuddy(self.notes_rests_slider)
        self.label_5.setBuddy(self.tempo)
        self.label.setBuddy(self.composition_mode)
        self.label_17.setBuddy(self.tempo)
        self.label_2.setBuddy(self.no_of_repeats)
        self.currentpercentage.setBuddy(self.currentslider)
        self.previouspercentage.setBuddy(self.previousslider)
        self.voice1label.setBuddy(self.voice1)
        self.voice2label.setBuddy(self.voice2)
        self.voice3label.setBuddy(self.voice3)
        self.voice4label.setBuddy(self.voice4)
        self.voice5label.setBuddy(self.voice5)
        self.voice6label.setBuddy(self.voice6)
        self.label_19.setBuddy(self.eighth_note_slider)
        self.label_15.setBuddy(self.half_note_slider)
        self.label_16.setBuddy(self.quarter_note_slider)
        self.label_20.setBuddy(self.sixteenth_note_slider)
        self.label_14.setBuddy(self.whole_note_slider)
        self.label_13.setBuddy(self.score_title)
        self.label_10.setBuddy(self.output_filename_2)
        self.label_7.setBuddy(self.output_foldername)
        self.label_9.setBuddy(self.output_filename_2)
        self.label_23.setBuddy(self.half_rest_slider)
        self.label_25.setBuddy(self.eighth_rest_slider)
        self.label_22.setBuddy(self.whole_rest_slider)
        self.label_24.setBuddy(self.quarter_rest_slider)
        self.label_26.setBuddy(self.sixteenth_rest_slider)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.key, self.time_enumerator)
        QWidget.setTabOrder(self.time_enumerator, self.time_denominator)
        QWidget.setTabOrder(self.time_denominator, self.tempo)
        QWidget.setTabOrder(self.tempo, self.notes_rests_slider)
        QWidget.setTabOrder(self.notes_rests_slider, self.currentslider)
        QWidget.setTabOrder(self.currentslider, self.previousslider)
        QWidget.setTabOrder(self.previousslider, self.whole_note_slider)
        QWidget.setTabOrder(self.whole_note_slider, self.half_note_slider)
        QWidget.setTabOrder(self.half_note_slider, self.quarter_note_slider)
        QWidget.setTabOrder(self.quarter_note_slider, self.eighth_note_slider)
        QWidget.setTabOrder(self.eighth_note_slider, self.sixteenth_note_slider)
        QWidget.setTabOrder(self.sixteenth_note_slider, self.generate_series)
        QWidget.setTabOrder(self.generate_series, self.voice1)
        QWidget.setTabOrder(self.voice1, self.voice2)
        QWidget.setTabOrder(self.voice2, self.voice3)
        QWidget.setTabOrder(self.voice3, self.voice4)
        QWidget.setTabOrder(self.voice4, self.voice5)
        QWidget.setTabOrder(self.voice5, self.voice6)
        QWidget.setTabOrder(self.voice6, self.whole_rest_slider)
        QWidget.setTabOrder(self.whole_rest_slider, self.half_rest_slider)
        QWidget.setTabOrder(self.half_rest_slider, self.quarter_rest_slider)
        QWidget.setTabOrder(self.quarter_rest_slider, self.eighth_rest_slider)
        QWidget.setTabOrder(self.eighth_rest_slider, self.sixteenth_rest_slider)
        QWidget.setTabOrder(self.sixteenth_rest_slider, self.score_title)
        QWidget.setTabOrder(self.score_title, self.output_filename_2)
        QWidget.setTabOrder(self.output_filename_2, self.output_foldername)
        QWidget.setTabOrder(self.output_foldername, self.open_file_explorer)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dodecaphony", None))
        self.groupBox.setTitle("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"General score settings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Key signature", None))
        self.percent_rests.setText(QCoreApplication.translate("MainWindow", u"0 % rests", None))
        self.percent_notes.setText(QCoreApplication.translate("MainWindow", u"100 % notes", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Time signature", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Repeat current note chance", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Notes/rests balance", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tempo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Template", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"bpm", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number of series repeats", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Repeat previous note chance", None))
        self.currentpercentage.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.previouspercentage.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Voices", None))
        self.voice1label.setText(QCoreApplication.translate("MainWindow", u"Voice 1", None))
        self.voice2label.setText(QCoreApplication.translate("MainWindow", u"Voice 2", None))
        self.voice3label.setText(QCoreApplication.translate("MainWindow", u"Voice 3", None))
        self.voice4label.setText(QCoreApplication.translate("MainWindow", u"Voice 4", None))
        self.voice5label.setText(QCoreApplication.translate("MainWindow", u"Voice 5", None))
        self.voice6label.setText(QCoreApplication.translate("MainWindow", u"Voice 6", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Series", None))
        self.series_label.setText(QCoreApplication.translate("MainWindow", u"Series preview:", None))
        self.generate_series.setText(QCoreApplication.translate("MainWindow", u"Generate series", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.dotted_eighth_note_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.eighth_note_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.dotted_whole_note_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.dotted_quarter_note.setText("")
        self.dotted_quarter_note_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.quarter_note_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.dotted_whole_note.setText("")
        self.whole_note_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.dotted_half_note.setText("")
        self.dotted_half_note_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_19.setText("")
        self.half_note_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_15.setText("")
        self.dotted_eighth_note.setText("")
        self.label_16.setText("")
        self.sixteenth_note_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_20.setText("")
        self.label_14.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Score title", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u".pdf", None))
        self.open_file_explorer.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Output folder", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Output filename", None))
        self.generate_score.setText(QCoreApplication.translate("MainWindow", u"Generate score", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Rests", None))
        self.sixteenth_rest_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.dotted_quarter_rest_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.dotted_half_rest.setText("")
        self.quarter_rest_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.eighth_rest_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.dotted_whole_rest_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_23.setText("")
        self.label_25.setText("")
        self.dotted_whole_rest.setText("")
        self.label_22.setText("")
        self.dotted_quarter_rest.setText("")
        self.label_24.setText("")
        self.whole_rest_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.half_rest_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_26.setText("")
        self.dotted_half_rest_pc.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.dotted_eighth_rest.setText("")
        self.dotted_eighth_rest_labe.setText(QCoreApplication.translate("MainWindow", u"0%", None))
    # retranslateUi

