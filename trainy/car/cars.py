from abc import ABC, abstractmethod
from engine import Engine
from wheels import Wheel


class Car(ABC):
    """
    Класс Car является Поставщиком если смотреть со стороны одного из Main(клиента)
    Для класса Car поставщиком является класс Engine.
    """

    def __init__(self, brand, engine: Engine, wheel: Wheel, performance=1, formula=None):
        self.brand = brand
        self.performance = performance
        self.formula = formula

        self.engine = engine
        self.wheel = wheel

        if formula is None:
            self.formula = self._default_avg_speed_calc

    def get_average_speed(self):
        return self.formula(self)

    def _default_avg_speed_calc(self, car):
        average_speed = car.engine.engine_load() * car.engine.engine_volume
        return average_speed





