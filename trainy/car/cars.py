from abc import ABC, abstractmethod
from engine import Engine, Diesel, Benzine


class Car(ABC):
    """
    Класс Car является Поставщиком если смотреть со стороны одного из Main(клиента)
    Для класса Car поставщиком является класс Engine.
    """

    def __init__(self, brand, engine: Engine, weight):
        self.brand = brand
        self.engine = engine
        self.weight = weight

    def get_average_speed(self):
        average_speed = self.engine.engine_load() * self.engine.engine_volume
        return average_speed


class Performance(Car):
    def __init__(self, *args, performance=1, **kwargs):
        self.performance = performance
        super().__init__(*args, **kwargs)

    def get_average_speed(self):
        ret = super().get_average_speed() * self.performance
        if isinstance(self.engine, Diesel):
            ret -= 2
        elif isinstance(self.engine, Benzine):
            ret += 2
        return ret








