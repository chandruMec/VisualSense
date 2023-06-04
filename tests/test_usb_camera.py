import unittest
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
