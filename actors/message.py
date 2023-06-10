class StartAcquisition:
    """
    StartAcquisition is message class to start acquisition
    """
    def __init__(self, src):
        """
        :param src: camera_id
        """
        self.src = src

class Frame:
    """
    Frame is message class which stores ImageQueue
    """
    def __init__(self,frame_queue):
        """
        :param frame_queue: it is frame queue
        """
        self.image_queue = frame_queue

class StopAcquisition:
    pass