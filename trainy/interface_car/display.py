from abc import ABC, abstractmethod

from tqdm import tqdm
from enums import CarStatus
from cars import Car, CarMT


class Display(ABC):
    def __init__(self, car: Car):
        self.car = car

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class DisplayForMyCar(Display):
    car: CarMT

    def __init__(self, car: CarMT):
        super().__init__(car)

        self.status_car = tqdm(desc=self.car.status, bar_format='Status Car : {desc}')
        self.rpm_bar = tqdm(total=self.car.engine.max_rpm, bar_format="RPM | {bar}{n_fmt} - {total_fmt}")
        self.gear_bar = tqdm(total=self.car.transmission.gear_length(), bar_format="Gear {n_fmt} of {total_fmt}")

    def show(self):
        self.rpm_bar.n = self.car.engine.get_current_rpm()

        self.rpm_bar.colour = 'RED' if self.car.status == CarStatus.rpm_cutoff else 'WHITE'

        self.gear_bar.n = self.car.transmission.get_current_gear()
        self.status_car.desc = self.car.status

        self.ref()

    def shutdown(self):
        self.status_car.close()
        self.rpm_bar.close()
        self.gear_bar.close()

    def ref(self):
        self.gear_bar.refresh()
        self.rpm_bar.refresh()
        self.status_car.refresh()
