
class Engine:
    def __init__(self, max_rpm):
        self.rpm = 0
        self.max_rpm = max_rpm

    def start_engine(self):
        self.rpm = 0 if self.rpm > 0 else 750