from actors import *
from image_sources import CameraFactory
from actors.message import StopAcquisition, StartAcquisition, Frame

# ImageAcquisition
# noinspection PyMethodMayBeStatic
class ImageAcquisitionActor(pykka.ThreadingActor):
    """
    ImageAcquisitionActor is pykka ThreadingActor which interacts with camera classes like USBCamera/GIGECamera
    """
    def __init__(self, camera_type):
        """
        :param camera_type: camera_type
        """
        super().__init__()
        self.camera = CameraFactory.create_camera(camera_type)

    def on_receive(self, message):
        """
        :param message: This message consist of Message Class like StartAcquisition/StopAcquisition/Frame
        :return: None
        """
        if isinstance(message, StartAcquisition):
            self.start_acquisition(message.src)
        elif isinstance(message, Frame):
            self.display(message.image_queue.get())
        elif isinstance(message, StopAcquisition):
            self.stop_acquisition()

    def start_acquisition(self, src):
        """
        start_acquisition is used to start the acquisition of your camera
        :param src: source of camera like camera_id
        :return: None
        """
        self.camera.start_acquisition(src,caller_actor=self.actor_ref)

    def stop_acquisition(self):
        """
        stop_acquisition is used to stop the acquisition of your camera
        :return: None
        """
        self.camera.stop_acquisition()

    def display(self,frame):
        """
        display is used to display the video window
        :param frame: current frame that is acquired from camera
        :return: None
        """
        cv2.imshow("frame", frame)
        cv2.waitKey(1)


# if __name__ == '__main__':
#     acquisition_usb = ImageAcquisitionActor.start(camera_type="usb")
#     acquisition_usb.tell(StartAcquisition(src=0))
#     time.sleep(5)
#     acquisition_usb.tell(StopAcquisition())
#     pykka.ActorRegistry.stop_all()
