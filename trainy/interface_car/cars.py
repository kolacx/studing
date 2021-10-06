from abc import ABC, abstractmethod
from engines import Engine
from transmissions import GearBox, AT, MT


class Car(ABC):
    def __init__(self, engine: Engine, transmission: GearBox):
        self.engine = engine
        self.transmission = transmission

    def start_engine(self):
        print('CAR - start_engine')
        self.engine.start_engine()

    def get_current_speed(self):
        speed = self.engine.get_rpm() * (64.3 / (((self.transmission.get_ratio() + 1) * 3.9) * 530.616))
        return round(speed, 2)

    def get_current_rpm_ratio(self):
        rpm = self.engine.rpm / self.transmission.ratio
        return rpm

    def get_max_rpm(self):
        return self.engine.get_max_rpm()

    def get_rpm(self):
        return self.engine.get_rpm()


class CarMT(Car):
    def __init__(self, engine, transmission: MT):
        super().__init__(engine, transmission)
        self.transmission = transmission    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def set_gear(self, gear):
        print(f'CAR MT - set_gear {gear}')
        self.transmission.set_gear(gear)

    def rpm_up(self):
        if self.engine.rpm >= self.engine.max_rpm:
            rpm = self.engine.rpm - 500
        else:
            rpm = self.engine.rpm + 100
        self.engine.set_rpm(rpm)

    def rpm_down(self):
        rpm = self.engine.rpm - 100
        self.engine.set_rpm(rpm)


class CarAT(Car):
    def __init__(self, engine, transmission: AT):
        super().__init__(engine, transmission)
        self.transmission = transmission

    def start_engine(self):
        print('CAR AT - start_engine')
        self.engine.start_engine()

    def set_gear(self, gear):
        print(f'CAR MT - set_gear {gear}')
        self.transmission.set_gear(gear)

    def up_gear(self):
        print('UP Gear')
        gear_up = self.transmission.get_current_gear() + 1
        self.set_gear(gear_up)

    def down_gear(self):
        print('DOWN Gear')
        gear_down = self.transmission.get_current_gear() - 1
        self.set_gear(gear_down)
