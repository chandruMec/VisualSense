from image_sources.image_source import Camera
import cv2
from threading import Thread


class USBCamera(Camera):
    def __init__(self, actor):
        super().__init__()
        self.usbcam = None
        self.frame_count = None
        self.fps = None
        self.height = None
        self.width = None
        self.source = None
        self.is_acquiring = False
        self.acquisition_thread = None
        self.usb_actor = actor

    def start_acquisition(self, src):
        if not self.is_acquiring:
            print("Opening your camera")
            self.usbcam = cv2.VideoCapture(src)
            if self.usbcam is None or not self.usbcam.isOpened():
                print('Warning: unable to open video source: ', src)
            else:
                self.source = self.usbcam.getBackendName()
                self.width = self.usbcam.get(cv2.CAP_PROP_FRAME_WIDTH)
                self.height = self.usbcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
                self.fps = self.usbcam.get(cv2.CAP_PROP_FPS)
                self.is_acquiring = True
                self.acquisition_thread = Thread(target=self.acquire_frames)
                self.acquisition_thread.start()

    def stop_acquisition(self):
        print("Closing your camera")
        if self.is_acquiring:
            self.is_acquiring = False
            self.acquisition_thread.join()  # Wait for the acquisition thread to finish
            self.usbcam.release()
            cv2.destroyAllWindows()

    def acquire_frames(self):
        while self.is_acquiring:
            ret, frame = self.usbcam.read()
            if not ret:
                break
            self.usb_actor.process_frame(frame)
