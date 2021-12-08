from abc import ABC, abstractmethod

from cars import Car, CarMT, CarAT
from engines import Engine
from transmissions import GearBox, AT, MT


class AbcCarFactory(ABC):
    def create_engine(self, max_rpm: int, idle: int) -> Engine:
        return Engine(max_rpm, idle)

    @abstractmethod
    def create_transmission(self, ratio_list: list, name: str) -> GearBox:
        pass

    @abstractmethod
    def create_car(self, engine: Engine, transmission: GearBox, name: str) -> Car:
        pass


class CarATCarFactory(AbcCarFactory):
    def create_transmission(self, ratio_list: list, name: str) -> AT:
        return AT(ratio_list, name)

    def create_car(self, engine: Engine, transmission: AT, name: str) -> CarAT:
        return CarAT(engine, transmission, name)


class CarMTCarFactory(AbcCarFactory):
    def create_transmission(self, ratio_list: list, name: str) -> MT:
        return MT(ratio_list, name)

    def create_car(self, engine: Engine, transmission: MT, name: str) -> CarMT:
        return CarMT(engine, transmission, name)
