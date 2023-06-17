from actors import *
from queue import Queue
class StartAcquisition:
    """
    StartAcquisition is message class to start acquisition
    """
    def __init__(self, src):
        """
        :param src: camera_id
        """
        self.src = src

class GetQueue:
    pass

class Frame:
    """
    Frame is message class which stores ImageQueue
    """
    def __init__(self,frame):
        """
        :param frame: it is a frame
        """
        self.frame = frame

class CamParams:
    def __init__(self,fps=None, height=None, width=None):
        self.fps = fps

class StopAcquisition:
    pass

class FpsGetter:
    def __init__(self):
        self.frame_count = 0
        self.start_time = time.time()
        self.fps = 0
        self.elapsed_time = None

    def get_fps(self):
        return self.fps

    def run_fps(self):
        self.frame_count += 1
        self.elapsed_time = time.time() - self.start_time
        if self.elapsed_time > 1.0:
            fps = self.frame_count / self.elapsed_time
            self.fps = fps
            self.frame_count = 0
            self.start_time = time.time()

class ProcessFrame:
    def __init__(self, processed_frame):
        self.processed_frame = processed_frame

# class SetProcess:
#     def __init__(self,correction):
#         self.correction = correction
