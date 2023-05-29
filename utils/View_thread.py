"""
Copyright (C) 2023 . All Rights Reserved. Mechmet Engineers.

File : View_thread.py

Description : This file contains GUI code in PySide6 configuration for the
framework.

Created on 27-4-2023.

Last modified at : 16-5-2023.
"""

from cv2 import (cvtColor, COLOR_BGR2RGB)
from PySide6.QtCore import (QThread, Signal)
from PySide6.QtWidgets import (QGraphicsScene)
from PySide6.QtGui import (QImage, QPixmap)
from PySide6.QtWidgets import (QGraphicsScene)


class DisplayThread(QThread):
    def __init__(self, proxy_model, ui):
        super(DisplayThread, self).__init__()
        self.model = proxy_model
        self.ui = ui

    @staticmethod
    def cv_to_qt(frame) -> QImage:
        """
        This function returns a QImage converted from Numpy array
            @param :
                image = numpy.ndarray
        """
        w, h, c = frame.shape
        image = cvtColor(frame, COLOR_BGR2RGB)
        image = QPixmap(QImage(image, h, w, h * c, QImage.Format_RGB888))
        pic = QGraphicsScene()
        pic.addPixmap(image)
        return pic

    image = Signal(QGraphicsScene)

    def run(self) -> None:
        while 1:
            frame = (next(self.model.frame_return().get()))

            if len(frame) > 0:

                self.ui.image_displayer.setScene(self.cv_to_qt(frame=frame))
                # self.ui.property_label.setText(txt)
