from abc import ABC, abstractmethod
from engine import Engine


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
    def __init__(self, *args, **kwargs):
        self.capacity = kwargs.pop('performance')
        super().__init__(*args, **kwargs)

    def get_average_speed(self):
        return super().get_average_speed() * self.capacity

# ========================================================


class MercedesPower(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_average_speed(self):
        return super().get_average_speed() * 1.1


class BMW1Power(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_average_speed(self):
        return super().get_average_speed() * 1.2


class BMW2Power(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_average_speed(self):
        return super().get_average_speed() * 1.3


class BMW3Power(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_average_speed(self):
        return super().get_average_speed() * 1.4


class Audi1Power(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_average_speed(self):
        return super().get_average_speed() * 1.5