

class Engine:
    def __init__(self, max_rpm):
        self._rpm = 0
        self._max_rpm = max_rpm

    def start(self):
        self.set_rpm(750)

    def stop(self):
        self.set_rpm(0)

    def set_rpm(self, rpm):
        self._rpm = rpm

    def get_rpm(self):
        return self._rpm

    def get_max_rpm(self):
        return self._max_rpm
