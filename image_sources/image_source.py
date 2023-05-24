class ImageSource:
    def acquire_image(self):
        raise NotImplementedError("acquire_image method must be implemented in child classes")

    def release_resources(self):
        pass

    def get_resolution(self):
        pass

    # Other shared methods and attributes can be added here
