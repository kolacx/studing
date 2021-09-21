from abc import ABC, abstractmethod


class Engine(ABC):
    ROTATION = 3000

    def __init__(self, power_kw):
        self.power_kw = power_kw

    def torque(self, coef: float):
        return (self.power_kw * 9550) / self.ROTATION


class Diesel(Engine):
    def __init__(self, *args):
        super().__init__(*args)
        self.name = 'Дизель'

    def torque(self, coef=1.0):
        return super().torque(coef) * coef


class Benzine(Engine):
    def __init__(self, *args):
        super().__init__(*args)
        self.name = 'Бензин'

