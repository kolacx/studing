from abc import ABC, abstractmethod
from engine import Engine


class Car(ABC):
    """
    Класс Car является Поставщиком если смотреть со стороны Main(клиента)
    Для класса Car поставщиком является класс Engine.
    """
    def __init__(self, brand, engine: Engine, weight):
        self.brand = brand
        self.engine = engine
        self.weight = weight
        self.average_speed = 100

    def get_average_speed(self):
        return self.average_speed
