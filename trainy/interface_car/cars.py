from abc import ABC, abstractmethod
from engines import Engine
from transmissions import GearBox, AT, MT


class Car(ABC):
    def __init__(self, engine: Engine, transmission: GearBox):
        self.engine = engine
        self.transmission = transmission

    @abstractmethod
    def start_car(self):
        pass

    @abstractmethod
    def stop_car(self):
        pass

    @abstractmethod
    def speed_up(self):
        pass

    @abstractmethod
    def speed_down(self):
        pass


class CarMT(Car):
    def start_car(self):
        self.engine.start_engine()

    def stop_car(self):
        self.engine.stop_engine()

    def shift_gear(self, gear):
        self.transmission.set_gear(gear)

    def speed_up(self):
        new_rpm = self.engine.get_current_rpm() + 100
        self.engine.set_rpm(new_rpm)

    def speed_down(self):
        new_rpm = self.engine.get_current_rpm() - 100
        self.engine.set_rpm(new_rpm)
        

class CarAT(Car):
    def start_car(self):
        self.engine.start_engine()

    def stop_car(self):
        self.engine.stop_engine()
