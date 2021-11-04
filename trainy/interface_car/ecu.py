from engines import Engine
from enums import CarStatus


class EngineECU:

    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.rpm = 750 if self.engine.rpm == 0 else 0

    def stop(self):
        self.engine.rpm = 0

    def set_rpm(self, rpm):

        cur_rpm = self.get_current_rpm()

        if self.get_current_rpm() == 0:
            return CarStatus.run_engine
        elif rpm > self.engine.max_rpm:
            self.set_rpm(rpm - 500)
            return CarStatus.rpm_cutoff
        elif rpm < 0:
            self.engine.rpm = 0
            return CarStatus.engine_down
        else:
            self.engine.rpm = rpm
            return CarStatus.rpm_up if cur_rpm < rpm else CarStatus.rpm_down

    def get_current_rpm(self):
        return self.engine.rpm
