from abc import ABC, abstractmethod

from cars import Car, CarMT, CarAT
from display import Display, DisplayMT, DisplayAT
from engines import Engine
from simulator import Simulator, SimulatorMT, SimulatorAT
from transmissions import GearBox, AT, MT


class AbcFactory(ABC):
    @abstractmethod
    def create_engine(self, max_rpm: int) -> Engine:
        pass

    @abstractmethod
    def create_transmission(self, ratio_list: list, name: str) -> GearBox:
        pass

    @abstractmethod
    def create_car(self, engine: Engine, transmission: GearBox, name: str) -> Car:
        pass

    @abstractmethod
    def create_display(self, car: Car) -> Display:
        pass

    @abstractmethod
    def create_simulator(self, car: Car, display: Display) -> Simulator:
        pass


class BmwATFactory(AbcFactory):
    def create_engine(self, max_rpm: int) -> Engine:
        return Engine(max_rpm)

    def create_transmission(self, ratio_list: list, name: str) -> AT:
        return AT(ratio_list, name)

    def create_car(self, engine: Engine, transmission: AT, name: str) -> CarAT:
        return CarAT(engine, transmission, name)

    def create_display(self, car: CarAT) -> DisplayAT:
        return DisplayAT(car)

    def create_simulator(self, car: CarAT, display: DisplayAT) -> SimulatorAT:
        return SimulatorAT(car, display)


class BmwMTFactory(AbcFactory):
    def create_engine(self, max_rpm: int) -> Engine:
        return Engine(max_rpm)

    def create_transmission(self, ratio_list: list, name: str) -> MT:
        return MT(ratio_list, name)

    def create_car(self, engine: Engine, transmission: MT, name: str) -> CarMT:
        return CarMT(engine, transmission, name)

    def create_display(self, car: CarMT) -> DisplayMT:
        return DisplayMT(car)

    def create_simulator(self, car: CarMT, display: DisplayMT) -> SimulatorMT:
        return SimulatorMT(car, display)
