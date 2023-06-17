"""
Qml-PySide2 UI module
"""

import sys
from actors import *
from actors.message import GetQueue, StartAcquisition, StopAcquisition
from actors.controller_actor import ControllerActor
from PySide2.QtCore import QObject, Signal, Slot, QTimer
from PySide2.QtGui import QGuiApplication, QImage
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuick import QQuickImageProvider



class QtWindow(QObject):
    """
    Class that connects Qml and PySide2 (Python) via Signals and Slots
    """

    frameChanged = Signal()

    def __init__(self, controller) -> None:
        super().__init__()
        self.timer = QTimer()
        self.dummy_image = QImage("../ui/assets/images/camera-desk-device-electronics.jpg")
        self.timer.timeout.connect(self.update_frame)
        self.controller_actor = controller.start()
        self.frame_queue = self.controller_actor.ask(GetQueue())

    @Slot()
    def start_cap(self) -> None:
        """
        Function to start Acquisition
        :return: None
        """
        print("You pressed Start Button")
        self.controller_actor.tell(StartAcquisition(src=0))
        self.timer.start(0)

    @Slot()
    def stop_cap(self) -> None:
        """
        Function to stop Acquisition
        :return: None
        """
        self.controller_actor.tell(StopAcquisition())
        print("You pressed Stop Button")
        self.timer.stop()

    @Slot(int, int)
    def apply_image_corrections(self, brightness_val, sharpen_val):
        correction ={"brightness":brightness_val,"sharpness":sharpen_val}
        print(correction)
        # self.controller_actor.tell(SetProcess(correction=correction))

    def update_frame(self) -> None:
        """
        Function to invoke frameChanged Signal for Qml to
        update the frame displayed
        :return: None
        """
        self.frameChanged.emit()

    def get_image(self):
        if self.frame_queue.qsize() > 0:
            frame = self.frame_queue.get()
            image = QImage(frame.data, frame.shape[1],
                           frame.shape[0], QImage.Format_RGB888)
            self.dummy_image = image.rgbSwapped()
            return image.rgbSwapped()
        return self.dummy_image

    def get_dummy(self):
        return self.dummy_image


class QmlFrameStreamer(QQuickImageProvider):
    """
    Class to convert and send Images from PySide2 (python) to Qml
    """

    def __init__(self, qt_window_obj):
        super().__init__(QQuickImageProvider.Image)
        self.qt_signal_bridge = qt_window_obj

    def requestImage(self, id: str, *args) -> QImage:
        """
        Function to convert a Frame (np.ndarray) to QImage
        :param id: string from Qt Qml call
        :param args:
        :return: Current frame in QImage format
        """
        if id == "webcam":
            return self.qt_signal_bridge.get_image()
        elif id == "refresh":
            return self.qt_signal_bridge.get_dummy()


if __name__ == '__main__':

    controller = ControllerActor()

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qt_window = QtWindow(controller=controller)
    frame2qml = QmlFrameStreamer(qt_window)

    engine.rootContext().setContextProperty("backend", qt_window)
    engine.addImageProvider("webcam", frame2qml)

    engine.load(str(qml_file))

    if not engine.rootObjects():
        sys.exit(-1)
    app.exec_()
    pykka.ActorRegistry.stop_all()
