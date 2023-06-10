from image_sources.image_source import Camera
import cv2
from queue import Queue
from actors.message import Frame
from threading import Thread


class USBCamera(Camera):
    def __init__(self):
        super().__init__()
        self.usbcam = None
        self.frame_count = None
        self.fps = None
        self.frame_queue = None
        self.height = None
        self.width = None
        self.source = None
        self.caller_actor = None
        self.is_acquiring = False
        self.acquisition_thread = None

    def start_acquisition(self, src, caller_actor):
        if not self.is_acquiring:
            print("Opening your camera")
            self.usbcam = cv2.VideoCapture(src)
            if self.usbcam is None or not self.usbcam.isOpened():
                print('Warning: unable to open video source: ', src)
            else:
                self.source = self.usbcam.getBackendName()
                self.caller_actor = caller_actor
                self.width = self.usbcam.get(cv2.CAP_PROP_FRAME_WIDTH)
                self.height = self.usbcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
                self.fps = self.usbcam.get(cv2.CAP_PROP_FPS)
                self.frame_queue = Queue(maxsize=2)
                self.is_acquiring = True
                self.acquisition_thread = Thread(target=self._acquire_frames)
                self.acquisition_thread.start()

    def stop_acquisition(self):
        print("Closing your camera")
        if self.is_acquiring:
            self.is_acquiring = False
            self.acquisition_thread.join()
            self.usbcam.release()

    def _acquire_frames(self):
        while self.is_acquiring:
            ret, frame = self.usbcam.read()
            if not ret:
                break
            self.frame_queue.put(frame)
            self.caller_actor.tell(Frame(frame=self.frame_queue))