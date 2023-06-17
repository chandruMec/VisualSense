from actors import *
from actors.message import Frame, FpsGetter, ProcessFrame
from queue import Queue

class ImageProcessingActor(pykka.ThreadingActor):
    def __init__(self,caller_actor):
        super().__init__()
        self.sharpen_value = None
        self.caller_actor = caller_actor
        self.default_sharpness=None
        self.brightness_alpha = 1.0
        self.brightness_beta = 0.0
        self.default_param = False

    def on_receive(self, message):
        if isinstance(message, Frame):
            frame = message.frame
            if not self.default_param:
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
                sharpness = np.mean((gray_frame - blurred_frame) ** 2)
                self.default_sharpness=sharpness
                self.set_default(sharpness=sharpness)
                self.default_param = True
            frame = self.process_frame(frame)
            self.caller_actor.tell(ProcessFrame(processed_frame=frame))

    def set_sharpen_value(self, sharpen_value):
        self.sharpen_value = sharpen_value

    def set_default(self,sharpness):
        self.set_sharpen_value(sharpen_value=sharpness)

    def process_frame(self, frame):
        if self.sharpen_value != self.default_sharpness:
            processed_frame = self.sharpen(frame, self.sharpen_value)
            return processed_frame
        else:
            return frame

    def sharpen(self, frame, sharpen_value):
        kernel = np.array([[-1,-1,-1], [-1,sharpen_value,-1], [-1,-1,-1]])
        sharpened_frame = cv2.filter2D(frame, -1, kernel)
        return sharpened_frame

    def display(self,frame):
        """
        display is used to display the video window
        :param frame: current frame that is acquired from camera
        :return: None
        """
        cv2.imshow("frame", frame)
        cv2.waitKey(1)

