import time
import unittest
import pykka
from actors.image_acquisition_actor import ImageAcquisitionActor
from actors.message import StartAcquisition, StopAcquisition


class ImageAcquisitionActorTest(unittest.TestCase):
    def setUp(self):
        self.image_acquire_ref = ImageAcquisitionActor.start(camera_type="usb")

    def tearDown(self):
        self.image_acquire_ref.tell(StopAcquisition())
        pykka.ActorRegistry.stop_all()

    def test_start_acquisition(self):
        self.image_acquire_ref.tell(StartAcquisition(src=0))
        time.sleep(10)
        self.image_acquire_ref.tell(StopAcquisition())

    def test_with_invalid_mode(self):
        self.image_acquire_ref.tell(StartAcquisition(src=-1))
        time.sleep(10)
        self.image_acquire_ref.tell(StopAcquisition())

    def test_close_open(self):
        self.image_acquire_ref.tell(StopAcquisition())
        self.image_acquire_ref.tell(StartAcquisition(src=0))
        time.sleep(10)
        self.image_acquire_ref.tell(StopAcquisition())

    def test_open_two(self):
        self.image_acquire_ref.tell(StartAcquisition(src=0))
        self.image_acquire_ref.tell(StartAcquisition(src=0))
        time.sleep(10)
        self.image_acquire_ref.tell(StopAcquisition())


if __name__ == '__main__':
    unittest.main()
