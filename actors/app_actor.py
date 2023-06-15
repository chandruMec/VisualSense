"""
Qml-PySide2 UI module
"""
import sys

from PySide2.QtCore import QObject, Signal, Slot, QTimer
from PySide2.QtGui import QGuiApplication, QImage
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuick import QQuickImageProvider

from actors import *


class QtWindow(QObject):
    """
    Class that connects Qml and PySide2 (Python) via Signals and Slots
    """

    frameChanged = Signal()

    def __init__(self) -> None:
        super().__init__()

        self.cap = cv2.VideoCapture(0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    @Slot()
    def start_cap(self) -> None:
        """
        Function to start Acquisition
        :return: None
        """
        print("You pressed Start Button")
        self.timer.start(0)

    @Slot()
    def stop_cap(self) -> None:
        """
        Function to stop Acquisition
        :return: None
        """
        print("You pressed Stop Button")
        self.timer.stop()

    def update_frame(self) -> None:
        """
        Function to invoke frameChanged Signal for Qml to
        update the frame displayed
        :return: None
        """
        self.frameChanged.emit()
    
    def get_image(self):
        ret, frame = self.cap.read()
        if ret:
            image = QImage(frame.data, frame.shape[1],
                           frame.shape[0], QImage.Format_RGB888)
            return image.rgbSwapped()
        return QImage("../ui/assets/images/dslr-camera-logo-design-png.png")
        

class QmlFrameStreamer(QQuickImageProvider):
    """
    Class to convert and send Images from PySide2 (python) to Qml
    """

    def __init__(self, qt_window_obj):
        super().__init__(QQuickImageProvider.Image)
        self.qt_signal_bridge = qt_window_obj

    def requestImage(self, q_msg: str, *args) -> QImage:
        """
        Function to convert a Frame (np.ndarray) to QImage
        :param q_msg: string from Qt Qml call
        :param args:
        :return: Current frame in QImage format
        """
        if q_msg == "webcam":
            return self.qt_signal_bridge.get_image()


class AppActor(pykka.ThreadingActor):
    """
    Main application actor
    """

    def __init__(self, qml_file_path: str) -> None:
        super().__init__()

        self.qml_file = qml_file_path
        self.qt_window = None

    def on_start(self) -> None:
        app = QGuiApplication(sys.argv)
        engine = QQmlApplicationEngine()

        self.qt_window = QtWindow()
        frame2qml = QmlFrameStreamer(self.qt_window)

        engine.rootContext().setContextProperty("backend", self.qt_window)
        engine.addImageProvider("webcam", frame2qml)

        engine.load(str(self.qml_file))

        if not engine.rootObjects():
            sys.exit(-1)

        app.exec_()
        self.actor_ref.stop()