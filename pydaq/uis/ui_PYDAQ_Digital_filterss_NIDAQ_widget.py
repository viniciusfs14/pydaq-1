# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PYDAQ_Digital_filterss_NIDAQ_widgetglznkG.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Digitalfilters_NIDAQ_widget(object):
    def setupUi(self, Digitalfilters_NIDAQ_widget):
        if not Digitalfilters_NIDAQ_widget.objectName():
            Digitalfilters_NIDAQ_widget.setObjectName(u"Digitalfilters_NIDAQ_widget")
        Digitalfilters_NIDAQ_widget.resize(922, 549)
        Digitalfilters_NIDAQ_widget.setStyleSheet(u"QWidget{\n"
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
"    image: url(:/imgs/drop_up_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rg"
                        "b(127, 167, 127);\n"
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
"    image: url(:/imgs/drop_down_arrow.png);\n"
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
"	background-color: rgb(77, 77, 77);\n"
""
                        "	\n"
"	border-top: 1.5px solid rgb(46, 46, 46);\n"
"	border-left: 1.5px solid rgb(46, 46, 46);\n"
"\n"
"	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
"	border-right: 1.5px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down{\n"
"	image: url(:/imgs/imgs/drop_down_arrow.png);\n"
"	width: 11px;\n"
"\n"
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
"	font: 12pt \"Helvetica\";\n"
"	"
                        "text-align:center;\n"
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
"\n"
"QPushBut"
                        "ton#reload_devices{\n"
"	image: url(:/imgs/imgs/reload.png);\n"
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
"}\n"
"\n"
"QPushButton#reload_devices:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(Digitalfilters_NIDAQ_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_6 = QWidget(Digitalfilters_NIDAQ_widget)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.filter_button = QPushButton(self.widget_6)
        self.filter_button.setObjectName(u"filter_button")
        self.filter_button.setMinimumSize(QSize(0, 30))
        self.filter_button.setMaximumSize(QSize(100, 30))

        self.gridLayout_7.addWidget(self.filter_button, 0, 0, 1, 1)

        self.fr_button = QPushButton(self.widget_6)
        self.fr_button.setObjectName(u"fr_button")
        self.fr_button.setMinimumSize(QSize(0, 30))
        self.fr_button.setMaximumSize(QSize(100, 30))

        self.gridLayout_7.addWidget(self.fr_button, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_6, 5, 0, 1, 1)

        self.line = QFrame(Digitalfilters_NIDAQ_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)

        self.left_side = QWidget(Digitalfilters_NIDAQ_widget)
        self.left_side.setObjectName(u"left_side")
        self.gridLayout_2 = QGridLayout(self.left_side)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.left_side)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.widget_2 = QWidget(self.left_side)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.channel_combo = QComboBox(self.widget_2)
        self.channel_combo.setObjectName(u"channel_combo")
        self.channel_combo.setMinimumSize(QSize(0, 22))
        self.channel_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_4.addWidget(self.channel_combo, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 1, 2, 1, 1)

        self.widget_8 = QWidget(self.left_side)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_9 = QGridLayout(self.widget_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.session_line = QDoubleSpinBox(self.widget_8)
        self.session_line.setObjectName(u"session_line")
        self.session_line.setMinimumSize(QSize(0, 22))
        self.session_line.setMaximumSize(QSize(16777215, 22))
        self.session_line.setDecimals(4)
        self.session_line.setSingleStep(0.010000000000000)
        self.session_line.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.session_line.setValue(10.000000000000000)

        self.gridLayout_9.addWidget(self.session_line, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_8, 7, 2, 1, 1)

        self.widget = QWidget(self.left_side)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.reload_devices = QPushButton(self.widget)
        self.reload_devices.setObjectName(u"reload_devices")
        self.reload_devices.setMinimumSize(QSize(22, 22))
        self.reload_devices.setMaximumSize(QSize(22, 22))

        self.gridLayout_3.addWidget(self.reload_devices, 0, 1, 1, 1)

        self.device_combo = QComboBox(self.widget)
        self.device_combo.setObjectName(u"device_combo")
        self.device_combo.setMinimumSize(QSize(0, 22))
        self.device_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_3.addWidget(self.device_combo, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 2, 1, 1)

        self.widget_9 = QWidget(self.left_side)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.yes_plot = QRadioButton(self.widget_9)
        self.ratio_plot = QButtonGroup(Digitalfilters_NIDAQ_widget)
        self.ratio_plot.setObjectName(u"ratio_plot")
        self.ratio_plot.addButton(self.yes_plot)
        self.yes_plot.setObjectName(u"yes_plot")
        self.yes_plot.setChecked(True)

        self.horizontalLayout_2.addWidget(self.yes_plot)

        self.no_plot = QRadioButton(self.widget_9)
        self.ratio_plot.addButton(self.no_plot)
        self.no_plot.setObjectName(u"no_plot")

        self.horizontalLayout_2.addWidget(self.no_plot)


        self.gridLayout_2.addWidget(self.widget_9, 9, 2, 2, 1, Qt.AlignLeft)

        self.widget_5 = QWidget(self.left_side)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_fr = QRadioButton(self.widget_5)
        self.ratio_fr = QButtonGroup(Digitalfilters_NIDAQ_widget)
        self.ratio_fr.setObjectName(u"ratio_fr")
        self.ratio_fr.addButton(self.yes_fr)
        self.yes_fr.setObjectName(u"yes_fr")
        self.yes_fr.setChecked(True)

        self.horizontalLayout.addWidget(self.yes_fr)

        self.no_fr = QRadioButton(self.widget_5)
        self.ratio_fr.addButton(self.no_fr)
        self.no_fr.setObjectName(u"no_fr")

        self.horizontalLayout.addWidget(self.no_fr)


        self.gridLayout_2.addWidget(self.widget_5, 8, 2, 1, 1, Qt.AlignLeft)

        self.widget_7 = QWidget(self.left_side)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_8 = QGridLayout(self.widget_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.sample_line = QDoubleSpinBox(self.widget_7)
        self.sample_line.setObjectName(u"sample_line")
        self.sample_line.setMinimumSize(QSize(0, 22))
        self.sample_line.setMaximumSize(QSize(16777215, 22))
        self.sample_line.setDecimals(4)
        self.sample_line.setSingleStep(0.010000000000000)
        self.sample_line.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.sample_line.setValue(0.500000000000000)

        self.gridLayout_8.addWidget(self.sample_line, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_7, 5, 2, 2, 1)

        self.label_10 = QLabel(self.left_side)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_10, 12, 0, 1, 1)

        self.label = QLabel(self.left_side)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(200, 30))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.widget_11 = QWidget(self.left_side)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.path_line = QLineEdit(self.widget_11)
        self.path_line.setObjectName(u"path_line")
        self.path_line.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_4.addWidget(self.path_line)

        self.browse_button = QPushButton(self.widget_11)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout_4.addWidget(self.browse_button)


        self.gridLayout_2.addWidget(self.widget_11, 12, 2, 2, 1)

        self.widget_3 = QWidget(self.left_side)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.terminal_combo = QComboBox(self.widget_3)
        self.terminal_combo.setObjectName(u"terminal_combo")
        self.terminal_combo.setMinimumSize(QSize(0, 22))
        self.terminal_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_5.addWidget(self.terminal_combo, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 2, 2, 1, 1)

        self.widget_10 = QWidget(self.left_side)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.yes_save = QRadioButton(self.widget_10)
        self.ratio_save = QButtonGroup(Digitalfilters_NIDAQ_widget)
        self.ratio_save.setObjectName(u"ratio_save")
        self.ratio_save.addButton(self.yes_save)
        self.yes_save.setObjectName(u"yes_save")
        self.yes_save.setChecked(True)

        self.horizontalLayout_3.addWidget(self.yes_save)

        self.no_save = QRadioButton(self.widget_10)
        self.ratio_save.addButton(self.no_save)
        self.no_save.setObjectName(u"no_save")

        self.horizontalLayout_3.addWidget(self.no_save)


        self.gridLayout_2.addWidget(self.widget_10, 11, 2, 1, 1, Qt.AlignLeft)

        self.line_7 = QFrame(self.left_side)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 0, 1, 14, 1)

        self.label_6 = QLabel(self.left_side)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_9 = QLabel(self.left_side)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_9, 11, 0, 1, 1)

        self.label_8 = QLabel(self.left_side)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_8, 10, 0, 1, 1)

        self.label_5 = QLabel(self.left_side)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_5, 8, 0, 1, 1)

        self.label_3 = QLabel(self.left_side)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.left_side)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_7 = QLabel(self.left_side)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 1)

        self.widget_4 = QWidget(self.left_side)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_6 = QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.type_filter = QComboBox(self.widget_4)
        self.type_filter.addItem("")
        self.type_filter.addItem("")
        self.type_filter.setObjectName(u"type_filter")
        self.type_filter.setMinimumSize(QSize(0, 22))
        self.type_filter.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_6.addWidget(self.type_filter, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_4, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.left_side, 3, 0, 1, 1)


        self.retranslateUi(Digitalfilters_NIDAQ_widget)

        QMetaObject.connectSlotsByName(Digitalfilters_NIDAQ_widget)
    # setupUi

    def retranslateUi(self, Digitalfilters_NIDAQ_widget):
        Digitalfilters_NIDAQ_widget.setWindowTitle(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Form", None))
        self.filter_button.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"FILTER", None))
        self.fr_button.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"FR", None))
        self.label_4.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Select your filter:", None))
        self.reload_devices.setText("")
        self.yes_plot.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Yes", None))
        self.no_plot.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"No", None))
        self.yes_fr.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Yes", None))
        self.no_fr.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"No", None))
        self.label_10.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Path", None))
        self.label.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Choose device:", None))
        self.browse_button.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Browse", None))
        self.yes_save.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Yes", None))
        self.no_save.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"No", None))
        self.label_6.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Sample Period (s)", None))
        self.label_9.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Save data?", None))
        self.label_8.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Plot data?", None))
        self.label_5.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Plot frequency response?", None))
        self.label_3.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Terminal Config.", None))
        self.label_2.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Choose channel:", None))
        self.label_7.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Session duration (s)", None))
        self.type_filter.setItemText(0, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"FIR", None))
        self.type_filter.setItemText(1, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"IIR", None))

    # retranslateUi

