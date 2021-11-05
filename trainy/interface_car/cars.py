from abc import ABC, abstractmethod
from engines import Engine
from transmissions import GearBox, AT, MT
from enums import CarStatus


class Car(ABC):
    def __init__(self, engine: Engine, transmission: GearBox):
        self.engine = engine
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
        self.status = CarStatus.info_run_engine

    def start(self):
        self.engine.start()
        self.status = CarStatus.engine_runed

    def stop(self):
        self.engine.stop()
        self.status = CarStatus.engine_stoped

    def speed_up(self):
        new_rpm = self.engine.get_current_rpm() + 100

        if self.engine.get_current_rpm() == 0:
            self.status = CarStatus.info_run_engine
        elif new_rpm > self.engine.max_rpm:
            self.engine.set_rpm(new_rpm - 500)
            self.status = CarStatus.info_rpm_cutoff
        else:
            self.engine.set_rpm(new_rpm)
            self.status = CarStatus.info_rpm_up

    def speed_down(self):
        new_rpm = self.engine.get_current_rpm() - 100

        if new_rpm < 0:
            self.engine.set_rpm(0)
            self.status = CarStatus.error_engine_down
        else:
            self.engine.set_rpm(new_rpm)
            self.status = CarStatus.info_rpm_down

    def shift_gear(self, gear):
        self.transmission.set_gear(gear)

    def gear_length(self):
        return self.transmission.gear_length()


class CarAT(Car):
    transmission: AT

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def speed_up(self):
        new_rpm = self.engine.get_current_rpm() + 100
        self.engine.set_rpm(new_rpm)

    def speed_down(self):
        new_rpm = self.engine.get_current_rpm() - 100
        self.engine.set_rpm(new_rpm)
