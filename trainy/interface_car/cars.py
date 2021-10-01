from abc import ABC, abstractmethod
from engines import Engine
from transmissions import GearBox, AT, MT


class Car(ABC):
    def __init__(self, engine: Engine, transmission: GearBox):
        self.engine = engine
        self.transmission = transmission

    def start_engine(self):
        self.engine.start_engine()

    def get_rpm(self):
        return self.engine.rpm

    def get_max_rpm(self):
        return self.engine.max_rpm

    def get_len_gearbox(self):
        return self.transmission.get_len_gearbox()

    def switch_gear(self, gear):
        self.transmission.set_gear(gear)

    def get_current_gear(self):
        return self.transmission.current_gear()

    def rpm_up(self):
        self.engine.rpm += 100

    def rpm_down(self):
        self.engine.rpm -= 100

    def get_current_speed(self):
        speed = self.engine.rpm * (64.3 / (((self.transmission.ratio + 1) * 3.9) * 530.616))
        return round(speed, 2)


class CarMT(Car):
    def __init__(self, engine, transmission: MT):
        super().__init__(engine, transmission)


class CarAT(Car):
    def __init__(self, engine, transmission: AT):
        super().__init__(engine, transmission)
