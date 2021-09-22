from abc import ABC, abstractmethod


class Engine(ABC):
    """
    Класс Engine является Поставщиком если смотреть со стороны класса Car
    Класс Car при этом является одним из клиентов.
    """

    ROTATION = 3000

    def __init__(self, engine_volume: float, power_hp: float, type: str):
        self.engine_volume = engine_volume
        self.power_hp = power_hp
        self.type = type
        self.rpm = 0

    def start(self):
        self.rpm = 800

    def stop(self):
        self.rpm = 0

    def engine_load(self):
        return self.ROTATION / self.power_hp

    def __repr__(self):
        return f"{self.type}@{self.power_hp}Hp"


class Diesel(Engine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Benzine(Engine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
