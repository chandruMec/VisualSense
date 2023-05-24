import unittest
from cv2 import VideoCapture, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT
from image_sources.usb_camera import USBCamera

class USBCameraTest(unittest.TestCase):

    def setUp(self):
        # Create an instance of the USBCamera class
        self.camera = USBCamera(camera_sdk=None)

    def test_open(self):
        # Test the open() method with a valid camera ID
        cam_id = 0
        result = self.camera.open(cam_id)
        self.assertTrue(result)

        # Test opening the camera with an invalid camera ID
        invalid_cam_id = -1
        result = self.camera.open(invalid_cam_id)
        self.assertFalse(result)

    def test_close(self):
        # Test the close() method when the camera is opened
        self.camera.open(cam_id=0)
        self.camera.close()
        self.assertFalse(self.camera.is_opened())

        # Test the close() method when the camera is not opened
        self.camera.close()
        self.assertFalse(self.camera.is_opened())

    def test_acquire_image(self):
        # Test acquiring an image from the camera
        self.camera.open(cam_id=0)
        image = self.camera.acquire_image()
        self.assertIsNotNone(image)

    def test_get_resolution(self):
        # Test getting the camera resolution
        self.camera.open(cam_id=0)
        width, height = self.camera.get_resolution()
        self.assertGreater(width, 0)
        self.assertGreater(height, 0)

    def test_is_opened(self):
        # Test the is_opened() method when the camera is opened
        self.camera.open(cam_id=0)
        self.assertTrue(self.camera.is_opened())

        # Test the is_opened() method when the camera is not opened
        self.camera.close()
        self.assertFalse(self.camera.is_opened())

    def test_release_resources(self):
        # Test releasing resources associated with the camera
        self.camera.open(cam_id=0)
        self.camera.release_resources()
        self.assertFalse(self.camera.is_opened())

    def tearDown(self):
        # Release any resources associated with the camera
        self.camera.release_resources()

if __name__ == '__main__':
    unittest.main()
