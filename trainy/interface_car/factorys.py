from abc import ABC, abstractmethod

from builders import TransmissionMTBuilder, TransmissionATBuilder, CarMTBuilder, CarATBuilder, SimulatorMTBuilder, \
    SimulatorATBuilder, DisplayMTBuilder, DisplayATBuilder
from cars import Car, CarMT, CarAT
from display import Display, DisplayMT, DisplayAT
from simulator import Simulator, SimulatorMT, SimulatorAT


# ========= Work with TRANSMISSION =========


class TransmissionFactory(ABC):
    @abstractmethod
    def create_transmission(self, ratio_list: list, name: str):
        pass


class TransmissionMTFactory(TransmissionFactory):
    def create_transmission(self, ratio_list: list, name: str):
        return TransmissionMTBuilder().set_ratio_list(ratio_list).set_name(name).build()


class TransmissionATFactory(TransmissionFactory):
    def create_transmission(self, ratio_list: list, name: str):
        return TransmissionATBuilder().set_ratio_list(ratio_list).set_name(name).build()


# ========= Work with CAR =========


class CarFactory(ABC):
    @abstractmethod
    def create_car(self, engine, transmission, name) -> Car:
        pass


class CarMTFactory(CarFactory):
    def create_car(self, engine, transmission, name) -> CarMT:
        return CarMTBuilder().set_engine(engine).set_transmission(transmission).set_name(name).build()


class CarATFactory(CarFactory):
    def create_car(self, engine, transmission, name) -> CarAT:
        return CarATBuilder().set_engine(engine).set_transmission(transmission).set_name(name).build()


# ========= Work with SIMULATOR =========


class SimulatorFactory(ABC):
    @abstractmethod
    def create_simulator(self, car: Car, display: Display) -> Simulator:
        pass


class SimulatorMTFactory(SimulatorFactory):
    def create_simulator(self, car: CarMT, display: DisplayMT) -> SimulatorMT:
        return SimulatorMTBuilder().set_car(car).set_display(display).build()


class SimulatorATFactory(SimulatorFactory):
    def create_simulator(self, car: CarAT, display: DisplayAT) -> SimulatorAT:
        return SimulatorATBuilder().set_car(car).set_display(display).build()


# ========= Work with DISPLAY =========


class DisplayFactory(ABC):
    @abstractmethod
    def create_display(self, car: Car) -> Display:
        pass


class DisplayMTFactory(DisplayFactory):
    def create_display(self, car: CarMT) -> DisplayMT:
        return DisplayMTBuilder().set_car(car).build()


class DisplayATFactory(DisplayFactory):
    def create_display(self, car: CarAT) -> DisplayAT:
        return DisplayATBuilder().set_car(car).build()

