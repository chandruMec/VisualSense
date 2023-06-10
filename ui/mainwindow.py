# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'front_end.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGraphicsView, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3, 0, Qt.AlignRight)

        self.Logout_btn = QPushButton(self.frame_4)
        self.Logout_btn.setObjectName(u"Logout_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logout_btn.sizePolicy().hasHeightForWidth())
        self.Logout_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.Logout_btn, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cam_name_list = QComboBox(self.frame_5)
        self.cam_name_list.setObjectName(u"cam_name_list")

        self.horizontalLayout_6.addWidget(self.cam_name_list)

        self.start_btn = QPushButton(self.frame_5)
        self.start_btn.setObjectName(u"start_btn")
        sizePolicy.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy)
        self.start_btn.setStyleSheet(u"background : Green")

        self.horizontalLayout_6.addWidget(self.start_btn)

        self.freeze_btn = QPushButton(self.frame_5)
        self.freeze_btn.setObjectName(u"freeze_btn")
        sizePolicy.setHeightForWidth(self.freeze_btn.sizePolicy().hasHeightForWidth())
        self.freeze_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.freeze_btn)

        self.settings = QComboBox(self.frame_5)
        self.settings.setObjectName(u"settings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.settings)

        self.Load_image_btn = QPushButton(self.frame_5)
        self.Load_image_btn.setObjectName(u"Load_image_btn")
        sizePolicy.setHeightForWidth(self.Load_image_btn.sizePolicy().hasHeightForWidth())
        self.Load_image_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.Load_image_btn)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.frame_7.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.component_name_line_edit = QLineEdit(self.frame_7)
        self.component_name_line_edit.setObjectName(u"component_name_line_edit")

        self.horizontalLayout_3.addWidget(self.component_name_line_edit)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.frame_8.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.image_type = QComboBox(self.frame_8)
        self.image_type.setObjectName(u"image_type")

        self.horizontalLayout_5.addWidget(self.image_type)

        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.save_as_accepted_btn = QPushButton(self.frame_5)
        self.save_as_accepted_btn.setObjectName(u"save_as_accepted_btn")
        sizePolicy.setHeightForWidth(self.save_as_accepted_btn.sizePolicy().hasHeightForWidth())
        self.save_as_accepted_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.save_as_accepted_btn)

        self.save_as_rejected_btn = QPushButton(self.frame_5)
        self.save_as_rejected_btn.setObjectName(u"save_as_rejected_btn")

        self.horizontalLayout_6.addWidget(self.save_as_rejected_btn)

        self.save_image_btn = QPushButton(self.frame_5)
        self.save_image_btn.setObjectName(u"save_image_btn")
        sizePolicy.setHeightForWidth(self.save_image_btn.sizePolicy().hasHeightForWidth())
        self.save_image_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.save_image_btn)

        self.radioButton = QRadioButton(self.frame_5)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_6.addWidget(self.radioButton)

        self.saved_name_line_edit = QLineEdit(self.frame_5)
        self.saved_name_line_edit.setObjectName(u"saved_name_line_edit")

        self.horizontalLayout_6.addWidget(self.saved_name_line_edit)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.frame_10.setLineWidth(0)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_10)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy2.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy2)
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Plain)
        self.frame_21.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.frame_21)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy2.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy2)
        self.frame_22.setFrameShape(QFrame.Panel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_22.setLineWidth(2)
        self.verticalLayout_10 = QVBoxLayout(self.frame_22)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.image_displayer = QGraphicsView(self.frame_22)
        self.image_displayer.setObjectName(u"image_displayer")
        sizePolicy2.setHeightForWidth(self.image_displayer.sizePolicy().hasHeightForWidth())
        self.image_displayer.setSizePolicy(sizePolicy2)
        self.image_displayer.setAutoFillBackground(True)
        self.image_displayer.setFrameShape(QFrame.Box)
        self.image_displayer.setFrameShadow(QFrame.Sunken)
        self.image_displayer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.image_displayer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.image_displayer.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.image_displayer.setRenderHints(QPainter.Antialiasing|QPainter.LosslessImageRendering|QPainter.NonCosmeticBrushPatterns|QPainter.SmoothPixmapTransform|QPainter.TextAntialiasing|QPainter.VerticalSubpixelPositioning)
        self.image_displayer.setDragMode(QGraphicsView.RubberBandDrag)
        self.image_displayer.setCacheMode(QGraphicsView.CacheBackground)
        self.image_displayer.setOptimizationFlags(QGraphicsView.DontAdjustForAntialiasing|QGraphicsView.DontSavePainterState|QGraphicsView.IndirectPainting)

        self.verticalLayout_10.addWidget(self.image_displayer)


        self.verticalLayout_8.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Box)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_23.setLineWidth(2)
        self.verticalLayout_9 = QVBoxLayout(self.frame_23)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.property_label = QLabel(self.frame_23)
        self.property_label.setObjectName(u"property_label")

        self.verticalLayout_9.addWidget(self.property_label)


        self.verticalLayout_8.addWidget(self.frame_23)


        self.verticalLayout_7.addWidget(self.frame_21)


        self.horizontalLayout_8.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Plain)
        self.frame_11.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.hide_btn = QPushButton(self.frame_11)
        self.hide_btn.setObjectName(u"hide_btn")
        sizePolicy.setHeightForWidth(self.hide_btn.sizePolicy().hasHeightForWidth())
        self.hide_btn.setSizePolicy(sizePolicy)
        self.hide_btn.setMinimumSize(QSize(20, 0))
        self.hide_btn.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_7.addWidget(self.hide_btn)

        self.frame_9 = QFrame(self.frame_11)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMaximumSize(QSize(500, 16777215))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.frame_9.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Plain)
        self.frame_12.setLineWidth(0)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.brightness_checkbox = QCheckBox(self.frame_12)
        self.brightness_checkbox.setObjectName(u"brightness_checkbox")

        self.horizontalLayout_9.addWidget(self.brightness_checkbox)

        self.brightness_slider = QSlider(self.frame_12)
        self.brightness_slider.setObjectName(u"brightness_slider")
        self.brightness_slider.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.brightness_slider.sizePolicy().hasHeightForWidth())
        self.brightness_slider.setSizePolicy(sizePolicy1)
        self.brightness_slider.setMinimumSize(QSize(250, 0))
        self.brightness_slider.setMinimum(1)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setSingleStep(1)
        self.brightness_slider.setOrientation(Qt.Horizontal)
        self.brightness_slider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_9.addWidget(self.brightness_slider)

        self.brightness_num = QSpinBox(self.frame_12)
        self.brightness_num.setObjectName(u"brightness_num")
        self.brightness_num.setEnabled(False)
        sizePolicy.setHeightForWidth(self.brightness_num.sizePolicy().hasHeightForWidth())
        self.brightness_num.setSizePolicy(sizePolicy)
        self.brightness_num.setMinimum(1)
        self.brightness_num.setMaximum(100)

        self.horizontalLayout_9.addWidget(self.brightness_num)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Plain)
        self.frame_13.setLineWidth(0)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.contrast_checkbox = QCheckBox(self.frame_13)
        self.contrast_checkbox.setObjectName(u"contrast_checkbox")

        self.horizontalLayout_10.addWidget(self.contrast_checkbox)

        self.contrast_slider = QSlider(self.frame_13)
        self.contrast_slider.setObjectName(u"contrast_slider")
        self.contrast_slider.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.contrast_slider.sizePolicy().hasHeightForWidth())
        self.contrast_slider.setSizePolicy(sizePolicy3)
        self.contrast_slider.setMinimumSize(QSize(250, 0))
        self.contrast_slider.setMinimum(1)
        self.contrast_slider.setMaximum(30)
        self.contrast_slider.setSingleStep(1)
        self.contrast_slider.setOrientation(Qt.Horizontal)
        self.contrast_slider.setTickPosition(QSlider.TicksBelow)
        self.contrast_slider.setTickInterval(5)

        self.horizontalLayout_10.addWidget(self.contrast_slider)

        self.contrast_num = QSpinBox(self.frame_13)
        self.contrast_num.setObjectName(u"contrast_num")
        self.contrast_num.setEnabled(False)
        sizePolicy.setHeightForWidth(self.contrast_num.sizePolicy().hasHeightForWidth())
        self.contrast_num.setSizePolicy(sizePolicy)
        self.contrast_num.setMinimum(1)
        self.contrast_num.setMaximum(30)

        self.horizontalLayout_10.addWidget(self.contrast_num)


        self.verticalLayout_5.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Plain)
        self.frame_14.setLineWidth(0)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gamma_checkbox = QCheckBox(self.frame_14)
        self.gamma_checkbox.setObjectName(u"gamma_checkbox")

        self.horizontalLayout_11.addWidget(self.gamma_checkbox)

        self.gamma_slider = QSlider(self.frame_14)
        self.gamma_slider.setObjectName(u"gamma_slider")
        self.gamma_slider.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.gamma_slider.sizePolicy().hasHeightForWidth())
        self.gamma_slider.setSizePolicy(sizePolicy3)
        self.gamma_slider.setMinimumSize(QSize(250, 0))
        self.gamma_slider.setMinimum(1)
        self.gamma_slider.setMaximum(30)
        self.gamma_slider.setValue(1)
        self.gamma_slider.setOrientation(Qt.Horizontal)
        self.gamma_slider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_11.addWidget(self.gamma_slider)

        self.gamma_num = QSpinBox(self.frame_14)
        self.gamma_num.setObjectName(u"gamma_num")
        self.gamma_num.setEnabled(False)
        sizePolicy.setHeightForWidth(self.gamma_num.sizePolicy().hasHeightForWidth())
        self.gamma_num.setSizePolicy(sizePolicy)
        self.gamma_num.setMinimum(1)
        self.gamma_num.setMaximum(30)

        self.horizontalLayout_11.addWidget(self.gamma_num)


        self.verticalLayout_5.addWidget(self.frame_14)

        self.frame_24 = QFrame(self.frame_9)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.smoothing_checkbox = QCheckBox(self.frame_24)
        self.smoothing_checkbox.setObjectName(u"smoothing_checkbox")

        self.horizontalLayout_16.addWidget(self.smoothing_checkbox)

        self.smoothing_slider = QSlider(self.frame_24)
        self.smoothing_slider.setObjectName(u"smoothing_slider")
        self.smoothing_slider.setEnabled(False)
        sizePolicy.setHeightForWidth(self.smoothing_slider.sizePolicy().hasHeightForWidth())
        self.smoothing_slider.setSizePolicy(sizePolicy)
        self.smoothing_slider.setMinimumSize(QSize(250, 0))
        self.smoothing_slider.setMinimum(1)
        self.smoothing_slider.setMaximum(10)
        self.smoothing_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_16.addWidget(self.smoothing_slider)

        self.smoothing_num = QSpinBox(self.frame_24)
        self.smoothing_num.setObjectName(u"smoothing_num")
        self.smoothing_num.setEnabled(False)
        sizePolicy.setHeightForWidth(self.smoothing_num.sizePolicy().hasHeightForWidth())
        self.smoothing_num.setSizePolicy(sizePolicy)
        self.smoothing_num.setMinimumSize(QSize(70, 0))
        self.smoothing_num.setMinimum(1)
        self.smoothing_num.setMaximum(10)

        self.horizontalLayout_16.addWidget(self.smoothing_num)


        self.verticalLayout_5.addWidget(self.frame_24)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Plain)
        self.frame_15.setLineWidth(0)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sharpning_checkbox = QCheckBox(self.frame_15)
        self.sharpning_checkbox.setObjectName(u"sharpning_checkbox")

        self.horizontalLayout_12.addWidget(self.sharpning_checkbox)

        self.sharpning_slider = QSlider(self.frame_15)
        self.sharpning_slider.setObjectName(u"sharpning_slider")
        self.sharpning_slider.setEnabled(False)
        sizePolicy.setHeightForWidth(self.sharpning_slider.sizePolicy().hasHeightForWidth())
        self.sharpning_slider.setSizePolicy(sizePolicy)
        self.sharpning_slider.setMinimumSize(QSize(250, 0))
        self.sharpning_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.sharpning_slider)

        self.sharp_num = QSpinBox(self.frame_15)
        self.sharp_num.setObjectName(u"sharp_num")
        self.sharp_num.setEnabled(False)
        sizePolicy.setHeightForWidth(self.sharp_num.sizePolicy().hasHeightForWidth())
        self.sharp_num.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.sharp_num)


        self.verticalLayout_5.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.frame_16.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_16)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.invert = QRadioButton(self.frame_16)
        self.invert.setObjectName(u"invert")

        self.verticalLayout_4.addWidget(self.invert)


        self.verticalLayout_5.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_9)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Plain)
        self.frame_17.setLineWidth(0)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.average_btn = QRadioButton(self.frame_18)
        self.average_btn.setObjectName(u"average_btn")

        self.horizontalLayout_13.addWidget(self.average_btn)

        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10, 0, Qt.AlignRight)

        self.no_image = QSpinBox(self.frame_18)
        self.no_image.setObjectName(u"no_image")
        self.no_image.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.no_image)


        self.horizontalLayout_15.addWidget(self.frame_18)


        self.verticalLayout_5.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_9)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Plain)
        self.frame_19.setLineWidth(0)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.save_settings = QPushButton(self.frame_19)
        self.save_settings.setObjectName(u"save_settings")
        sizePolicy.setHeightForWidth(self.save_settings.sizePolicy().hasHeightForWidth())
        self.save_settings.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.save_settings)

        self.reset_to_saved_settings = QPushButton(self.frame_19)
        self.reset_to_saved_settings.setObjectName(u"reset_to_saved_settings")
        sizePolicy.setHeightForWidth(self.reset_to_saved_settings.sizePolicy().hasHeightForWidth())
        self.reset_to_saved_settings.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.reset_to_saved_settings)

        self.default_settings = QPushButton(self.frame_19)
        self.default_settings.setObjectName(u"default_settings")
        sizePolicy.setHeightForWidth(self.default_settings.sizePolicy().hasHeightForWidth())
        self.default_settings.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.default_settings)


        self.verticalLayout_5.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_9)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Plain)
        self.frame_20.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_14 = QPushButton(self.frame_20)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.frame_20)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.frame_20)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.pushButton_16)


        self.verticalLayout_5.addWidget(self.frame_20)


        self.horizontalLayout_7.addWidget(self.frame_9)


        self.horizontalLayout_8.addWidget(self.frame_11)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMaximumSize(QSize(16777215, 10))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.brightness_slider.valueChanged.connect(self.brightness_num.setValue)
        self.contrast_slider.valueChanged.connect(self.contrast_num.setValue)
        self.gamma_slider.valueChanged.connect(self.gamma_num.setValue)
        self.smoothing_slider.valueChanged.connect(self.smoothing_num.setValue)
        self.sharpning_slider.valueChanged.connect(self.sharp_num.setValue)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Front Pannel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Logo ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"company name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login status", None))
        self.Logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.freeze_btn.setText(QCoreApplication.translate("MainWindow", u"Freeze", None))
        self.Load_image_btn.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Component", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Image Type", None))
        self.save_as_accepted_btn.setText(QCoreApplication.translate("MainWindow", u"Save as Accepted", None))
        self.save_as_rejected_btn.setText(QCoreApplication.translate("MainWindow", u"Save as Rejected", None))
        self.save_image_btn.setText(QCoreApplication.translate("MainWindow", u"Save Image ", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Import File Name ", None))
        self.property_label.setText(QCoreApplication.translate("MainWindow", u"Properties : ", None))
        self.hide_btn.setText(QCoreApplication.translate("MainWindow", u"H\n"
"I\n"
"D\n"
"E", None))
        self.brightness_checkbox.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.contrast_checkbox.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.gamma_checkbox.setText(QCoreApplication.translate("MainWindow", u"Gamma", None))
        self.smoothing_checkbox.setText(QCoreApplication.translate("MainWindow", u"Smoothing", None))
        self.sharpning_checkbox.setText(QCoreApplication.translate("MainWindow", u"Sharpning", None))
        self.invert.setText(QCoreApplication.translate("MainWindow", u"Invert ", None))
        self.average_btn.setText(QCoreApplication.translate("MainWindow", u"Averaging", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"No.of Images", None))
        self.save_settings.setText(QCoreApplication.translate("MainWindow", u"Save Parameters", None))
        self.reset_to_saved_settings.setText(QCoreApplication.translate("MainWindow", u"Reset to Last Saved ", None))
        self.default_settings.setText(QCoreApplication.translate("MainWindow", u"Default Parameters", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

