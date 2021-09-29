from engines import Engine
from transmissions import GearBox


class Car:
    def __init__(self, engine: Engine, transmission: GearBox):
        self.engine = engine
        self.transmission = transmission
