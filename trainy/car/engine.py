from abc import ABC, abstractmethod


class Engine(ABC):
    ROTATION = 3000

    def __init__(self, power_kw):
        self.power_kw = power_kw

    def torque(self, coef=None):
        return (self.power_kw * 9550) / self.ROTATION


class Diesel(Engine):
    def torque(self, coef=None):
        return super().torque(coef) * coef


class Benzine(Engine):
    pass
