from abc import ABC, abstractmethod

from tqdm import tqdm
from enums import CarStatus
from cars import Car, CarMT


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


car_status_map = {
    CarStatus.engine_runed: 'Engine is Started. Bo-Bo-Bo-Bo-Bo-Bo-Bo',
    CarStatus.engine_stoped: 'Engine is Stoped...',
    CarStatus.info_run_engine: bcolors.FAIL + 'First Start Engine <S>' + bcolors.ENDC,
    CarStatus.info_rpm_cutoff: bcolors.FAIL + 'RATA-TA-TA-TA-TA-TA-TA-TA' + bcolors.ENDC,
    CarStatus.info_rpm_up: 'RPM UP',
    CarStatus.info_rpm_down: 'RPM DOWN',
    CarStatus.error_engine_down: bcolors.FAIL + 'Engine is down. See you at retake' + bcolors.ENDC
}


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

        self.status_car = tqdm(desc=car_status_map.get(self.car.status), bar_format='Status Car : {desc}')
        self.rpm_bar = tqdm(total=self.car.engine.max_rpm, bar_format="RPM | {bar}{n_fmt} - {total_fmt}")
        self.gear_bar = tqdm(total=self.car.transmission.gear_length(), bar_format="Gear {n_fmt} of {total_fmt}")

    def show(self):
        self.rpm_bar.n = self.car.engine.get_current_rpm()

        self.rpm_bar.colour = 'RED' if self.car.status == CarStatus.info_rpm_cutoff else 'WHITE'

        self.gear_bar.n = self.car.transmission.get_current_gear()
        self.status_car.desc = car_status_map.get(self.car.status)

        self.ref()

    def shutdown(self):
        self.status_car.close()
        self.rpm_bar.close()
        self.gear_bar.close()

    def ref(self):
        self.gear_bar.refresh()
        self.rpm_bar.refresh()
        self.status_car.refresh()
