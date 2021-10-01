from engines import Engine
from transmissions import GearBox, ControlMT, MT, AT, ControlAT


class Car:
    def __init__(self, engine: Engine, transmission: GearBox):
        self.engine = engine
        self.transmission = transmission





















    # def start_engine(self):
    #     self.engine.start_engine()
    #
    # def get_len_gearbox(self):
    #     return self.transmission.get_len_gearbox()
    #
    # def switch_gear(self, gear):
    #     self.transmission.set_gear(gear)
    #
    # def get_current_gear(self):
    #     return self.transmission.current_gear()
    #
    # def rpm_up(self):
    #     pass
    #
    # def rpm_down(self):
    #     pass