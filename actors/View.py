"""
Copyright (C) 2022 . All Rights Reserved. Mechmet Engineers.

File : View.py

Description : This file contains GUI code in PySide6 configuration for the
framework.

Created on 27-4-2023.

Last modified at : 29-5-2023.
"""

from __future__ import (unicode_literals)


__all__ = []
__author__ = "Chandrakanth G"
__version__ = 0.4

from os import (_exit)

from PySide6.QtWidgets import (QMainWindow)
from pykka import (ThreadingActor)

# from View_thread import (DisplayThread)
from ui.mainwindow import Ui_MainWindow
from utils.message_stock import message_stock


class View(QMainWindow, ThreadingActor):

    def __init__(self, controller: object):
        """

        @type controller: object
        """
        super(View, self).__init__()
        self.ui = Ui_MainWindow()
        self.acquisition = False
        self.ui.setupUi(self)
        self.controller = controller
        # self.get_cam_names()
        self._btn_connection()
        self._slider_connect()

    def closeEvent(self, event) -> None:
        self.controller.ask(message_stock(8))
        # self.display_thread.terminate()
        event.accept()
        _exit(0)

    def _start_function(self):
        if not self.acquisition:
            self.acquisition = True
            self.controller.ask(
                {message_stock(1): self.ui.cam_name_list.currentIndex()})
            # self.display_thread.start()
            self.ui.start_btn.setText("Stop")
            self.ui.start_btn.setStyleSheet("background : Red")

        else:
            self.acquisition = False
            self.controller.ask({message_stock(0): message_stock(1)})
            self.ui.start_btn.setText("Start")
            self.ui.start_btn.setStyleSheet("background : Green")

    def _hide_settings(self):

        self.ui.frame_9.setMaximumWidth(
            0) if self.ui.frame_9.width() > 5 else self.ui.frame_9.\
            setMaximumWidth(421)

    def _btn_connection(self):

        self.ui.invert.clicked.connect(self._invert_btn)
        self.ui.hide_btn.clicked.connect(self._hide_settings)
        self.ui.start_btn.clicked.connect(self._start_function)
        self.ui.average_btn.clicked.connect(self._average_control)

    def _slider_connect(self):
        self.ui.brightness_slider.valueChanged.connect(
            self._brightness_control)
        self.ui.contrast_slider.valueChanged.connect(self._contrast_control)
        self.ui.gamma_slider.valueChanged.connect(self._gamma_control)
        self.ui.smoothing_slider.valueChanged.connect(self._smooth_control)
        self.ui.sharpning_slider.valueChanged.connect(self._sharping_control)

    def _invert_btn(self):
        self.controller.ask({message_stock(0): message_stock(2)})

    def _gamma_control(self, num):
        self.controller.ask({message_stock(3): num})
        self.ui.gamma_num.setValue(num)

    def _brightness_control(self, num):
        self.controller.ask({message_stock(4): num})
        self.ui.brightness_num.setValue(num)

    def _contrast_control(self, num):
        self.controller.ask({message_stock(4): num})
        self.ui.contrast_num.setValue(num)

    def _smooth_control(self, num):
        self.controller.ask({message_stock(5): num})
        self.ui.smoothing_num.setValue(num)

    def _sharping_control(self, num):
        self.controller.ask({message_stock(6): num})
        self.ui.sharp_num.setValue(num)

    def _average_control(self):
        self.controller.ask({message_stock(7): str(self.ui.no_image.value())})

    def _get_cam_names(self):
        names = self.controller.proxy().get_camera_names().get()
        self.ui.cam_name_list.addItem(names)


if __name__ == "__main__":
    pass
