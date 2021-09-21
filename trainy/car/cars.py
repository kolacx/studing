from abc import ABC, abstractmethod
from engine import Engine


class Car(ABC):

    def __init__(self, brand, engine: Engine, weight):
        self.brand = brand
        self.weight = weight
        self.engine = engine

    def average_speed(self):
        return (self.engine.power_kw * self.engine.torque()) / self.weight


class Distance:
    def __init__(self, car: Car):
        self.car = car

    def distance(self, km):
        return (km / self.car.average_speed()) * 60


class DistanceMercedes(Distance):

    def distance(self, km):
        return ((km / self.car.average_speed()) * 60) - 6
