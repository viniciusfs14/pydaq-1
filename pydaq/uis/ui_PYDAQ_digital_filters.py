# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwNlNMM.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)


class Ui_DigitalFilters(object):
    def setupUi(self, DigitalFilters):
        if not DigitalFilters.objectName():
            DigitalFilters.setObjectName(u"DigitalFilters")
        DigitalFilters.resize(707, 610)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DigitalFilters.sizePolicy().hasHeightForWidth())
        DigitalFilters.setSizePolicy(sizePolicy)
        DigitalFilters.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(64, 64, 64);\n"
"}\n"
"\n"
"QTabWidget::pane { \n"
"   border: 1px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  	background-color: rgb(77, 77, 77);\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  	background-color: rgb(140, 140, 140);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:selected:hover {\n"
"  	background-color: rgb(140, 140, 140);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:hover {\n"
"  	background-color: rgb(109, 109, 109);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:middle {\n"
"	border-right: 1px dashed rgb(166, 166, 166);\n"
"	border-left: 1px dashed rgb(166, 166, 166);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar:"
                        ":tab:last {\n"
"	border-top-right-radius: 10px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:first {\n"
"	border-top-left-radius: 10px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(77, 77, 77);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:focus{\n"
"    background-color: rgb(140, 140, 140);\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"	background-color: rgb(77, 77, 77);\n"
"	\n"
"	border-top: 1.5px solid rgb(46, 46, 46);\n"
"	border-left: 1.5px solid rgb(46, 46, 46);\n"
"\n"
"	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
"	border-right: 1.5px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"    image: url(:/imgs/imgs/drop_up_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px sol"
                        "id rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"    image: url(:/imgs/imgs/drop_down_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"	background-color: rgb(64, 64, 64);\n"
"}\n"
"\n"
"QWidget{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: rgb(77, "
                        "77, 77);\n"
"	\n"
"	border-top: 1.5px solid rgb(46, 46, 46);\n"
"	border-left: 1.5px solid rgb(46, 46, 46);\n"
"\n"
"	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
"	border-right: 1.5px solid rgb(166, 166, 166);\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down{\n"
"	\n"
"	width: 11px;\n"
"	image: url(:/sim/drop_down_arrow.png);\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 2px solid rgb(127, 167, 127);\n"
"	border-left: 2px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 2px solid rgb(0, 0, 0);\n"
"	border-right: 2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox::drop-down:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QComboBox::drop-down:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(0, 79, 0);\n"
"\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"\n"
"	\n"
"	font: 12pt \"Helve"
                        "tica\";\n"
"	text-align:center;\n"
"}\n"
"\n"
"QWidget{\n"
"	font: 12pt \"Helvetica\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(77, 77, 77);\n"
"	border-top: 1.5px solid rgb(46, 46, 46);\n"
"	border-left: 1.5px solid rgb(46, 46, 46);\n"
"\n"
"	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
"	border-right: 1.5px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"	border-radius: 6px;\n"
"	border-top: 1.5px solid rgb(0, 0, 0);\n"
"	border-left: 1.5px solid rgb(0, 0, 0);\n"
"\n"
"	border-bottom: 1.5px solid rgb(160, 160, 160);\n"
"	border-right: 1.5px solid rgb(160, 160, 160);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked:hover{\n"
"	background-color: #9F9F9F;\n"
"}\n"
"\n"
"QRadioButton::indicator::pressed{\n"
"	border: 1.5px solid #505050\n"
"}\n"
""
                        "\n"
"QPushButton#reload_devices{\n"
"    image: url(:/sim/reload.png);\n"
"	width: 11px;\n"
"	background-color: rgb(0, 79, 0);\n"
"\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"\n"
"	\n"
"	font: 12pt \"Helvetica\";\n"
"	text-align:center;\n"
"}\n"
"\n"
"QPushButton#reload_devices:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"	image: url(:/sim/reload.png);\n"
"}\n"
"\n"
"QPushButton#reload_devices:{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(DigitalFilters)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_6 = QGridLayout(self.widget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.no_fr = QCheckBox(self.widget_3)
        self.buttonGroup = QButtonGroup(DigitalFilters)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.no_fr)
        self.no_fr.setObjectName(u"no_fr")

        self.gridLayout_6.addWidget(self.no_fr, 0, 1, 1, 1, Qt.AlignRight)

        self.yes_fr = QCheckBox(self.widget_3)
        self.buttonGroup.addButton(self.yes_fr)
        self.yes_fr.setObjectName(u"yes_fr")

        self.gridLayout_6.addWidget(self.yes_fr, 0, 2, 1, 1, Qt.AlignRight)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 8, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.reload_devices = QPushButton(self.widget_2)
        self.reload_devices.setObjectName(u"reload_devices")
        self.reload_devices.setMaximumSize(QSize(22, 22))
        self.reload_devices.setBaseSize(QSize(0, 0))
        self.reload_devices.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.reload_devices, 0, 2, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 6, 0, 1, 1)

        self.fiirwidget = QWidget(self.widget)
        self.fiirwidget.setObjectName(u"fiirwidget")
        self.gridLayout_4 = QGridLayout(self.fiirwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_8 = QLineEdit(self.fiirwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_4.addWidget(self.lineEdit_8, 3, 3, 1, 1, Qt.AlignRight)

        self.lineEdit_7 = QLineEdit(self.fiirwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_4.addWidget(self.lineEdit_7, 2, 3, 1, 1, Qt.AlignRight)

        self.label_4 = QLabel(self.fiirwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_9 = QLabel(self.fiirwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.fiirwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_4.addWidget(self.lineEdit_5, 0, 3, 1, 1, Qt.AlignRight)

        self.label_10 = QLabel(self.fiirwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_8 = QLabel(self.fiirwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.fiirwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_4.addWidget(self.lineEdit_6, 1, 3, 1, 1, Qt.AlignRight)

        self.label_12 = QLabel(self.fiirwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.fiirwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_4.addWidget(self.comboBox_3, 4, 3, 1, 1)


        self.gridLayout.addWidget(self.fiirwidget, 4, 0, 1, 1)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 5, 0, 1, 1)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 9, 0, 1, 1)

        self.iirwidget = QWidget(self.widget)
        self.iirwidget.setObjectName(u"iirwidget")
        self.gridLayout_3 = QGridLayout(self.iirwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.iirwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.iirwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)

        self.firOrder = QLineEdit(self.iirwidget)
        self.firOrder.setObjectName(u"firOrder")

        self.gridLayout_3.addWidget(self.firOrder, 1, 1, 1, 1, Qt.AlignRight)

        self.label_5 = QLabel(self.iirwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.lowfrequency = QLineEdit(self.iirwidget)
        self.lowfrequency.setObjectName(u"lowfrequency")

        self.gridLayout_3.addWidget(self.lowfrequency, 3, 1, 1, 1, Qt.AlignRight)

        self.label_7 = QLabel(self.iirwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)

        self.highfrequency = QLineEdit(self.iirwidget)
        self.highfrequency.setObjectName(u"highfrequency")

        self.gridLayout_3.addWidget(self.highfrequency, 4, 1, 1, 1, Qt.AlignRight)

        self.Fs = QLineEdit(self.iirwidget)
        self.Fs.setObjectName(u"Fs")

        self.gridLayout_3.addWidget(self.Fs, 2, 1, 1, 1, Qt.AlignRight)

        self.label_11 = QLabel(self.iirwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.iirwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_3.addWidget(self.comboBox_2, 5, 1, 1, 1)


        self.gridLayout.addWidget(self.iirwidget, 3, 0, 1, 1)

        self.mid = QWidget(self.widget)
        self.mid.setObjectName(u"mid")
        self.horizontalLayout = QHBoxLayout(self.mid)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.mid)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.typeFilter = QComboBox(self.mid)
        self.typeFilter.addItem("")
        self.typeFilter.addItem("")
        self.typeFilter.setObjectName(u"typeFilter")

        self.horizontalLayout.addWidget(self.typeFilter)


        self.gridLayout.addWidget(self.mid, 1, 0, 1, 1)

        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 7, 0, 1, 1)

        self.bottom = QWidget(self.widget)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bottom.sizePolicy().hasHeightForWidth())
        self.bottom.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.bottom)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.filterButton = QPushButton(self.bottom)
        self.filterButton.setObjectName(u"filterButton")

        self.horizontalLayout_3.addWidget(self.filterButton)

        self.closeButton = QPushButton(self.bottom)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.gridLayout.addWidget(self.bottom, 11, 0, 1, 1, Qt.AlignBottom)


        self.gridLayout_2.addWidget(self.widget, 2, 0, 1, 1)

        DigitalFilters.setCentralWidget(self.centralwidget)

        self.retranslateUi(DigitalFilters)

        QMetaObject.connectSlotsByName(DigitalFilters)
    # setupUi

    def retranslateUi(self, DigitalFilters):
        DigitalFilters.setWindowTitle(QCoreApplication.translate("DigitalFilters", u"MainWindow", None))
        self.no_fr.setText(QCoreApplication.translate("DigitalFilters", u"Yes", None))
        self.yes_fr.setText(QCoreApplication.translate("DigitalFilters", u"No", None))
        self.label_13.setText(QCoreApplication.translate("DigitalFilters", u"Plot frequence response?", None))
        self.reload_devices.setText("")
        self.label_2.setText(QCoreApplication.translate("DigitalFilters", u"Select your arduino board:", None))
#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("DigitalFilters", u"<html><head/><body><p>Please, select your arduino board</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_8.setText(QCoreApplication.translate("DigitalFilters", u"130", None))
        self.lineEdit_7.setText(QCoreApplication.translate("DigitalFilters", u"100", None))
        self.label_4.setText(QCoreApplication.translate("DigitalFilters", u"Enter filter numtaps:", None))
        self.label_9.setText(QCoreApplication.translate("DigitalFilters", u"Low (Hz):", None))
        self.lineEdit_5.setText(QCoreApplication.translate("DigitalFilters", u"3", None))
        self.label_10.setText(QCoreApplication.translate("DigitalFilters", u"High (Hz):", None))
        self.label_8.setText(QCoreApplication.translate("DigitalFilters", u"Fs:", None))
        self.lineEdit_6.setText(QCoreApplication.translate("DigitalFilters", u"1000", None))
        self.label_12.setText(QCoreApplication.translate("DigitalFilters", u"Type:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("DigitalFilters", u"HALF-BAND ", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("DigitalFilters", u"HIGHPASS", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("DigitalFilters", u"BANDPASS", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("DigitalFilters", u"LOWPASS", None))

        self.label_3.setText(QCoreApplication.translate("DigitalFilters", u"Enter filter order (N):", None))
        self.label_6.setText(QCoreApplication.translate("DigitalFilters", u"Low (Hz):", None))
        self.firOrder.setText(QCoreApplication.translate("DigitalFilters", u"4", None))
        self.label_5.setText(QCoreApplication.translate("DigitalFilters", u"Fs:", None))
        self.lowfrequency.setText(QCoreApplication.translate("DigitalFilters", u"100", None))
        self.label_7.setText(QCoreApplication.translate("DigitalFilters", u"High (Hz):", None))
        self.highfrequency.setText(QCoreApplication.translate("DigitalFilters", u"150", None))
        self.Fs.setText(QCoreApplication.translate("DigitalFilters", u"1000", None))
        self.label_11.setText(QCoreApplication.translate("DigitalFilters", u"Type:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("DigitalFilters", u"BUTTERWORTH", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("DigitalFilters", u"CHEBYSHEV", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("DigitalFilters", u"BESSEL", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("DigitalFilters", u"CAUER", None))

        self.label.setText(QCoreApplication.translate("DigitalFilters", u"Select your filter:", None))
        self.typeFilter.setItemText(0, QCoreApplication.translate("DigitalFilters", u"FIR", None))
        self.typeFilter.setItemText(1, QCoreApplication.translate("DigitalFilters", u"IIR", None))

        self.filterButton.setText(QCoreApplication.translate("DigitalFilters", u"FILTER", None))
        self.closeButton.setText(QCoreApplication.translate("DigitalFilters", u"CLOSE", None))
    # retranslateUi

