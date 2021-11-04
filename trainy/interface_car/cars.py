from abc import ABC, abstractmethod
from ecu import EngineECU
from transmissions import GearBox, AT, MT
from enums import CarStatus


class Car(ABC):
    def __init__(self, engine_ecu: EngineECU, transmission: GearBox):
        self.engine_ecu = engine_ecu
        self.transmission = transmission

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def speed_up(self):
        pass

    @abstractmethod
    def speed_down(self):
        pass


class CarMT(Car):
    transmission: MT

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.status = CarStatus.run_engine

    def start(self):
        self.engine_ecu.start()
        self.status = CarStatus.started

    def stop(self):
        self.engine_ecu.stop()
        self.status = CarStatus.stoped

    def speed_up(self):
        new_rpm = self.engine_ecu.get_current_rpm() + 100
        self.status = self.engine_ecu.set_rpm(new_rpm)

    def speed_down(self):
        new_rpm = self.engine_ecu.get_current_rpm() - 100
        self.status = self.engine_ecu.set_rpm(new_rpm)

    def shift_gear(self, gear):
        self.transmission.set_gear(gear)

    def gear_length(self):
        return self.transmission.gear_length()


class CarAT(Car):
    transmission: AT

    def start(self):
        self.engine_ecu.start()

    def stop(self):
        self.engine_ecu.stop()

    def speed_up(self):
        new_rpm = self.engine_ecu.get_current_rpm() + 100
        self.engine_ecu.set_rpm(new_rpm)

    def speed_down(self):
        new_rpm = self.engine_ecu.get_current_rpm() - 100
        self.engine_ecu.set_rpm(new_rpm)
