import unittest

from pykka import ActorRegistry
import image_sources.usb_camera as usb_camera
import actors.image_acquisition_actor as image_acquisition_actor


class TestUSBCamera(unittest.TestCase):
    def setUp(self):
        usb_acquire=image_acquisition_actor.ImageAcquisitionActor(camera_type="usb")
        self.camera_ref = usb_camera.USBCamera(usb_acquire)

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
    unittest.main()
