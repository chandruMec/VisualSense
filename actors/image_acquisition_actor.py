import pykka
import cv2

class ImageAcquisitionActor(pykka.ThreadingActor):
    def __init__(self, image_source):
        super().__init__()
        self.image_source = image_source

    def on_start(self):
        self.image_source.open()

    def on_stop(self):
        self.image_source.close()

    def acquire_image(self):
        while self.image_source.is_opened():
            image = self.image_source.acquire_image()
            # Process the acquired image here
            # Send the acquired image to other actors for further processing

    def cleanup(self):
        self.stop()


# Usage example:
camera_sdk = ...  # Initialize camera SDK

image_source = ImageSourceFactory.create_image_source('usb_camera', camera_sdk)
acquisition_actor = ImageAcquisitionActor.start(image_source, use_daemon_thread=False).proxy()

acquisition_actor.acquire_image()