from abc import ABC, abstractmethod


class Camera(ABC):
    def __init__(self):
        self.is_acquiring = False

    @abstractmethod
    def start_acquisition(self,*args, **kwargs):
        pass

    @abstractmethod
    def stop_acquisition(self):
        pass



