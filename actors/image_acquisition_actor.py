from actors import *
from image_sources import CameraFactory
from actors.message import StopAcquisition, StartAcquisition, Frame

# ImageAcquisition
# noinspection PyMethodMayBeStatic
class ImageAcquisitionActor(pykka.ThreadingActor):
    def __init__(self, camera_type):
        super().__init__()
        self.camera = CameraFactory.create_camera(camera_type)

    def on_receive(self, message):
        if isinstance(message, StartAcquisition):
            self.start_acquisition(message.src)
        elif isinstance(message, Frame):
            self.display(message.image_queue.get())
        elif isinstance(message, StopAcquisition):
            self.stop_acquisition()

    def start_acquisition(self, src):
        self.camera.start_acquisition(src,caller_actor=self.actor_ref)

    def stop_acquisition(self):
        self.camera.stop_acquisition()

    def display(self,frame):
        cv2.imshow("frame", frame)
        cv2.waitKey(1)


if __name__ == '__main__':
    acquisition_usb = ImageAcquisitionActor.start(camera_type="usb")
    acquisition_usb.tell(StartAcquisition(src=0))
    time.sleep(5)
    acquisition_usb.tell(StopAcquisition())
    pykka.ActorRegistry.stop_all()
