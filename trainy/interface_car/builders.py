from abc import ABC, abstractmethod

from cars import CarMT, CarAT, Car
from display import DisplayMT, DisplayAT
from engines import Engine
from simulator import Simulator, SimulatorMT, SimulatorAT
from transmissions import MT, AT, GearBox


class EngineBuilder:
    def set_max_rpm(self, max_rpm):
        self.max_rpm = max_rpm
        return self

    def build(self) -> Engine:
        return Engine(self.max_rpm)


# ========= Work with TRANSMISSION =========


class TransmissionBuilder(ABC):
    @abstractmethod
    def set_ratio_list(self, ratio_list: list):
        pass

    @abstractmethod
    def set_name(self, name: str):
        pass

    @abstractmethod
    def build(self):
        pass


class TransmissionMTBuilder(TransmissionBuilder):
    def set_ratio_list(self, ratio_list: list):
        self.ratio_list = ratio_list
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def build(self):
        return MT(self.ratio_list, self.name)


class TransmissionATBuilder(TransmissionBuilder):
    def set_ratio_list(self, ratio_list: list):
        self.ratio_list = ratio_list
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def build(self):
        return AT(self.ratio_list, self.name)


# ========= Work with CAR =========


class CarBuilder(ABC):
    def set_engine(self, engine: Engine):
        self.engine = engine
        return self

    @abstractmethod
    def set_transmission(self, transmission: GearBox):
        pass

    def set_name(self, name: str):
        self.name = name
        return self

    @abstractmethod
    def build(self):
        pass


class CarMTBuilder(CarBuilder):
    def set_transmission(self, transmission: MT):
        self.transmission = transmission
        return self

    def build(self) -> CarMT:
        return CarMT(self.engine, self.transmission, self.name)


class CarATBuilder(CarBuilder):
    def set_transmission(self, transmission: AT):
        self.transmission = transmission
        return self

    def build(self) -> CarAT:
        return CarAT(self.engine, self.transmission, self.name)


# ========= Work with SIMULATOR =========


class SimulatorBuilder(ABC):
    @abstractmethod
    def set_car(self, car: Car):
        pass

    @abstractmethod
    def set_display(self, display):
        pass

    @abstractmethod
    def build(self) -> Simulator:
        pass


class SimulatorMTBuilder(SimulatorBuilder):
    def set_car(self, car: CarMT):
        self.car = car
        return self

    def set_display(self, display: DisplayMT):
        self.display = display
        return self

    def build(self) -> SimulatorMT:
        return SimulatorMT(self.car, self.display)


class SimulatorATBuilder(SimulatorBuilder):
    def set_car(self, car: CarAT):
        self.car = car
        return self

    def set_display(self, display: DisplayAT):
        self.display = display
        return self

    def build(self) -> SimulatorAT:
        return SimulatorAT(self.car, self.display)


# ========= Work with DISPLAY =========


class DisplayBuilder(ABC):
    @abstractmethod
    def set_car(self, car: Car):
        pass

    @abstractmethod
    def build(self):
        pass


class DisplayMTBuilder(DisplayBuilder):
    def set_car(self, car: CarMT):
        self.car = car
        return self

    def build(self) -> DisplayMT:
        return DisplayMT(self.car)


class DisplayATBuilder(DisplayBuilder):
    def set_car(self, car: CarAT):
        self.car = car
        return self

    def build(self) -> DisplayAT:
        return DisplayAT(self.car)
