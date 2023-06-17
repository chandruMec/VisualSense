import time
import pykka
from queue import Queue
from actors import *
from actors.image_processing_actor import ImageProcessingActor
from actors.image_acquisition_actor import ImageAcquisitionActor
from actors.message import StopAcquisition,StartAcquisition, Frame, ProcessFrame, FpsGetter, GetQueue


class ControllerActor(pykka.ThreadingActor):
    def __init__(self):
        super().__init__()

        self.processed_queue = Queue()

        # Create the child actors
        self.fps_cal = FpsGetter()
        self.image_acquisition_actor = ImageAcquisitionActor.start(camera_type="usb",caller_actor=self.actor_ref)
        self.processing_actor = ImageProcessingActor.start(caller_actor=self.actor_ref)

    def on_receive(self, message):
        if isinstance(message, StartAcquisition):
            print("Started Acq")
            self.image_acquisition_actor.tell(StartAcquisition(src=0))

        elif isinstance(message,StopAcquisition):
            self.image_acquisition_actor.tell(StopAcquisition())

        elif isinstance(message, Frame):
            self.processing_actor.tell(Frame(frame=message.frame))

        elif isinstance(message, ProcessFrame):
            self.fps_cal.run_fps()
            fps = self.fps_cal.get_fps()
            processed_frame = cv2.putText(message.processed_frame, "Fps : "+str(int(fps)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8 , (255,255,255), 3)
            self.processed_queue.put(processed_frame)
            # self.display(processed_frame)

        elif isinstance(message, GetQueue):
            return self.processed_queue


    def display(self,frame):
        """
        display is used to display the video window
        :param frame: current frame that is acquired from camera
        :return: None
        """
        cv2.imshow("frame", frame)
        cv2.waitKey(1)


