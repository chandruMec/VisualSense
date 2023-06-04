import unittest

from pykka import ActorRegistry
from image_sources.usb_camera import USBCamera
from actors.image_acquisition_actor import ImageAcquisitionActor
class TestUSBCamera(unittest.TestCase):
    def setUp(self):
        usb_acquire=ImageAcquisitionActor(camera_type="usb")
        self.camera_ref = USBCamera(usb_acquire)

    def tearDown(self):
        ActorRegistry.stop_all()

    def test_start_and_stop_acquisition(self):
        self.camera_ref.start_acquisition(src=0)
        self.assertTrue(self.camera_ref.is_acquiring)

        self.camera_ref.stop_acquisition()
        self.assertFalse(self.camera_ref.is_acquiring)

    def test_camera_param(self):

        self.camera_ref.start_acquisition(src=0)
        self.assertEqual(self.camera_ref.fps,30)
        self.assertGreater(self.camera_ref.width,0)
        self.assertGreater(self.camera_ref.height, 0)
        self.camera_ref.stop_acquisition()

    def test_close_open(self):

        self.camera_ref.stop_acquisition()
        self.assertFalse(self.camera_ref.is_acquiring)

        self.camera_ref.start_acquisition(src=0)
        self.assertTrue(self.camera_ref.is_acquiring)

        self.camera_ref.stop_acquisition()
        self.assertFalse(self.camera_ref.is_acquiring)

    def test_invalid_source_id(self):
        result = self.camera_ref.start_acquisition(src=-1)
        self.assertFalse(result)


if __name__ == '__main__':
=======
from image_sources.usb_camera import USBCamera
import numpy



class test_usb(unittest.TestCase):

    usb_cam = USBCamera()
    
    def test_open(self):
       self.assertTrue(self.usb_cam.open(0))

    def test_is_opened(self):
        self.assertTrue(self.usb_cam.is_opened(0))

    def test_camera(self):
        self.assertIsInstance(self.usb_cam.cameras(),list)
        print(self.usb_cam.cameras())

    def test_image(self):
        self.assertIsInstance(self.usb_cam.image(0),numpy.ndarray)

 
    def test_get_resolution(self):
       
        self.assertIsInstance(self.usb_cam.get_resolution(0),tuple)
        

    def test_close(self):
        self.usb_cam.close(0)
        self.assertFalse(self.usb_cam.is_opened(0))


   
    






if __name__ == "__main__":
    unittest.main()
