from cv2 import VideoCapture, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT
from image_sources.image_source import ImageSource


class USBCamera(ImageSource):
    def __init__(self, camera_sdk):
        self.camera_sdk = camera_sdk
        self.cam = None

    def open(self,cam_id):
        # Open USB camera using the camera SDK 
        self.cam = VideoCapture(cam_id)
        return self.cam.isOpened()
        

    def close(self):
        # Close the USB camera and release resources
        if self.cam != None:
            self.cam.release()

    def acquire_image(self):
        # Acquire image from the USB camera using the camera SDK
        return self.cam.read()

    def release_resources(self):
        # Release any resources associated with the USB camera
        self.close()

    def get_resolution(self):
        # Get the resolution of the USB camera
        return self.cam.get(CAP_PROP_FRAME_WIDTH), self.cam.get(CAP_PROP_FRAME_HEIGHT)
    
    def is_opened(self):
        return self.cam.isOpened()
    