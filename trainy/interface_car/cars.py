from abc import ABC, abstractmethod
from engines import Engine
from transmissions import GearBox, AT, MT
from enums import CarStatus, ATGearboxModes


class Car(ABC):
    def __init__(self, engine: Engine, transmission: GearBox, model):
        self.model = model
        self.engine = engine
        self.transmission = transmission

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def speed_up(self, acsel):
        pass

    @abstractmethod
    def speed_down(self, acsel):
        pass

    def __str__(self):
        return f'{self.model} | Engine: {self.engine.get_max_rpm()} | Transmission: {self.transmission.name}'


class CarMT(Car):
    transmission: MT

    def __init__(self, engine, transmission, name, cutoff=500, engine_idle=750):
        super().__init__(engine, transmission, name)
        self.cutoff = cutoff
        self.engine_idle = engine_idle

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def speed_up(self, acsel):
        new_rpm = self.engine.get_rpm() + acsel
        self.engine.set_rpm(new_rpm)

    def speed_down(self, acsel):
        new_rpm = self.engine.get_rpm() - acsel
        self.engine.set_rpm(new_rpm)

    def shift_gear(self, gear):
        self.transmission.set_gear(gear)

    def gear_length(self):
        return self.transmission.gear_length()


class CarAT(CarMT):
    transmission: AT

    def __init__(self, engine, transmission, name, rpm_for_down=1000, rpm_for_up=1000,
                 default_shift_height=3000, default_shift_low=1000):

        super().__init__(engine, transmission, name)
        self.mode = ATGearboxModes.parking

        self.rpm_for_down = rpm_for_down
        self.rpm_for_up = rpm_for_up
        self.default_shift_height = default_shift_height
        self.default_shift_low = default_shift_low

    def requirements_for_up_shift(self, rpm):
        if rpm < self.default_shift_height:
            return False
        elif self.transmission.get_gear() == self.transmission.gear_length():
            return False
        else:
            return True

    def speed_up(self, acsel):
        if self.mode == ATGearboxModes.drive:
            new_rpm = self.engine.get_rpm() + acsel

            if new_rpm < self.engine.get_max_rpm():
                self.engine.set_rpm(new_rpm)
            else:
                new_rpm -= self.cutoff
                self.engine.set_rpm(new_rpm)

            if self.requirements_for_up_shift(new_rpm):
                self.transmission.up_set_gear()
                self.engine.set_rpm(new_rpm - self.rpm_for_up)

    def requirements_for_down_shift(self, rpm):
        if rpm > self.default_shift_low:
            return False
        elif self.transmission.get_gear() == 1:
            return False
        else:
            return True

    def speed_down(self, acsel):
        if self.mode == ATGearboxModes.drive:
            new_rpm = self.engine.get_rpm() - acsel

            if new_rpm > self.engine_idle:
                self.engine.set_rpm(new_rpm)
            else:
                self.engine.set_rpm(0)

            if self.requirements_for_down_shift(new_rpm):
                self.transmission.down_set_gear()
                self.engine.set_rpm(new_rpm + self.rpm_for_down)

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
