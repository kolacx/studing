from abc import ABC, abstractmethod


class Engine(ABC):
    ROTATION = 3000

    def __init__(self, engine_volume: float, power_kw: float):
        self.engine_volume = engine_volume
        self.power_kw = power_kw
        self.rpm = 0

    def start(self):
        self.rpm = 800

    def stop(self):
        self.rpm = 0

    def torque(self):
        return (self.power_kw * 9550) / self.ROTATION


class Diesel(Engine):
    def __init__(self, engine_volume: float, power_kw: float, power_index):
        super().__init__(engine_volume, power_kw)
        self.type = 'Дизель'
        self.power_index = power_index

    def torque(self):
        return (super().torque() * 1.1) / self.power_index

    def __repr__(self):
        return f"Power: {self.power_kw}, Type: {self.type}"


class Benzine(Engine):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = 'Бензин'

    def __repr__(self):
        return f"Power: {self.power_kw}, Type: {self.type}"
