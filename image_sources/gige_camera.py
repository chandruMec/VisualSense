from image_sources.image_source import Camera


class GigeCamera(Camera):
    def start_acquisition(self, ip):
        print("Starting GigE camera acquisition...")
        print("param1:", ip)
        self.is_acquiring = True

    def stop_acquisition(self):
        print("Stopping GigE camera acquisition...")
        self.is_acquiring = False