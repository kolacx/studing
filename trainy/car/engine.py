from abc import ABC, abstractmethod


class Engine(ABC):
    """
    Класс Engine является Поставщиком если смотреть со стороны класса Car
    Класс Car при этом является клиентом.
    """

    ROTATION = 3000

    def __init__(self, engine_volume: float, power_kw: float, type: str):
        self.engine_volume = engine_volume
        self.power_kw = power_kw
        self.type = type
        self.rpm = 0

    def start(self):
        self.rpm = 800

    def stop(self):
        self.rpm = 0

    def __repr__(self):
        return f"{self.type}@{self.power_kw}Kw"


class Diesel(Engine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Benzine(Engine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
