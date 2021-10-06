from abc import ABC, abstractmethod
from engines import Engine
from transmissions import GearBox, AT, MT


class Car(ABC):
    def __init__(self, engine: Engine, transmission: GearBox):
        self.engine = engine
        self.transmission = transmission


class CarMT(Car):
    def __init__(self, engine, transmission: MT):
        super().__init__(engine, transmission)
        self.transmission = transmission    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def start_engine(self):
        print('CAR MT - start_engine')
        self.engine.start_engine()

    def set_gear(self, gear):
        print(f'CAR MT - set_gear {gear}')
        self.transmission.set_gear(gear)

    def get_current_speed(self):
        speed = self.engine.rpm * (64.3 / (((self.transmission.ratio + 1) * 3.9) * 530.616))
        return round(speed, 2)


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
