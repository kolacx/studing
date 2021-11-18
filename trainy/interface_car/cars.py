from abc import ABC, abstractmethod
from engines import Engine
from transmissions import GearBox, AT, MT
from enums import CarStatus, ATGearboxModes


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

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def speed_up(self):
        new_rpm = self.engine.get_rpm() + 100
        self.engine.set_rpm(new_rpm)

    def speed_down(self):
        new_rpm = self.engine.get_rpm() - 100
        self.engine.set_rpm(new_rpm)

    def shift_gear(self, gear):
        self.transmission.set_gear(gear)

    def gear_length(self):
        return self.transmission.gear_length()


class CarAT(CarMT):
    transmission: AT

    def __init__(self, car, display):
        super().__init__(car, display)
        self.mode = ATGearboxModes.parking

    def __requirements_for_up_shift(self, rpm):
        if rpm < 3000:
            return False
        elif self.transmission.get_gear() == self.transmission.gear_length():
            return False
        else:
            return True

    def speed_up(self):
        if self.mode == ATGearboxModes.drive:
            new_rpm = self.engine.get_rpm() + 100
            cutoff = 500

            if new_rpm < self.engine.get_max_rpm():
                self.engine.set_rpm(new_rpm)
            else:
                new_rpm -= cutoff
                self.engine.set_rpm(new_rpm)

            if self.__requirements_for_up_shift(new_rpm):
                self.transmission.up_set_gear()
                self.engine.set_rpm(new_rpm - 1000)

    def __requirements_for_down_shift(self, rpm):
        if rpm > 1000:
            return False
        elif self.transmission.get_gear() == 1:
            return False
        else:
            return True

    def speed_down(self):
        if self.mode == ATGearboxModes.drive:
            new_rpm = self.engine.get_rpm() - 100

            if new_rpm > 750:
                self.engine.set_rpm(new_rpm)
            else:
                self.engine.set_rpm(0)

            if self.__requirements_for_down_shift(new_rpm):
                self.transmission.down_set_gear()
                self.engine.set_rpm(new_rpm + 1000)

    def up_gear(self):
        if self.mode == ATGearboxModes.manual:
            self.transmission.up_set_gear()

    def down_gear(self):
        if self.mode == ATGearboxModes.manual:
            self.transmission.down_set_gear()

    def manual_mode(self):
        self.mode = ATGearboxModes.manual

    def drive_mode(self):
        self.mode = ATGearboxModes.drive
        self.transmission.set_gear(1)

    def neutral_mode(self):
        self.mode = ATGearboxModes.neutral
        self.transmission.set_gear(0)

    def parking_mode(self):
        self.mode = ATGearboxModes.parking
        self.transmission.set_gear(0)
