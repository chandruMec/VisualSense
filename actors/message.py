class StartAcquisition:
    def __init__(self, src):
        self.src = src

class Frame:
    def __init__(self,frame):
        self.image_queue = frame

class StopAcquisition:
    pass