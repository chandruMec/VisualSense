from image_sources.usb_camera import USBCamera
from image_sources.gige_camera import GigeCamera
import cv2
camera_registry = {"usb": USBCamera, "gige": GigeCamera}

class CameraFactory:

    @staticmethod
    def create_camera(camera_type):
        if camera_type in camera_registry:
            camera_class = camera_registry[camera_type]
            return camera_class()
        else:
            raise ValueError("Invalid camera type")