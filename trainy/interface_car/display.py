from abc import ABC, abstractmethod

from tqdm import tqdm
from enums import CarStatus, ATGearboxModes
from cars import Car, CarMT, CarAT


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
    CarStatus.started: 'Engine is Started. Bo-Bo-Bo-Bo-Bo-Bo-Bo',
    CarStatus.stopped: 'Engine is Stoped...',
    # CarStatus.info_run_engine: bcolors.FAIL + 'First Start Engine <S>' + bcolors.ENDC,
    # CarStatus.info_rpm_cutoff: bcolors.FAIL + 'RATA-TA-TA-TA-TA-TA-TA-TA' + bcolors.ENDC,
    # CarStatus.info_rpm_up: 'RPM UP',
    # CarStatus.info_rpm_down: 'RPM DOWN',
    # CarStatus.error_engine_down: bcolors.FAIL + 'Engine is down. See you at retake' + bcolors.ENDC
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


class DisplayMT(Display):
    car: CarMT

    def __init__(self, car: CarMT):
        super().__init__(car)

        self.car_info_bar = tqdm(desc=f"{self.car}", bar_format="You at: {desc}")
        self.rpm_bar = tqdm(total=self.car.engine.get_max_rpm(), bar_format="RPM | {bar}{n_fmt} - {total_fmt}")
        self.gear_bar = tqdm(total=self.car.transmission.gear_length(), bar_format="Gear {n_fmt} of {total_fmt}")

    def show(self):
        self.rpm_bar.n = self.car.engine.get_rpm()
        self.gear_bar.n = self.car.transmission.get_gear()

        self.ref()

    def shutdown(self):
        self.rpm_bar.close()
        self.gear_bar.close()
        self.car_info_bar.close()

    def ref(self):
        self.gear_bar.refresh()
        self.rpm_bar.refresh()


transmission_AT_mode = {
    ATGearboxModes.neutral: 'Neutral',
    ATGearboxModes.parking: 'Parking',
    ATGearboxModes.drive: 'Drive',
    ATGearboxModes.reverse: 'Revers',
    ATGearboxModes.manual: 'Manual'
}


class DisplayAT(Display):
    car: CarAT

    def __init__(self, car: CarAT):
        super().__init__(car)

        self.car_info_bar = tqdm(desc=f"{self.car}", bar_format="You at: {desc}")
        self.status_bar = tqdm(desc=transmission_AT_mode.get(self.car.mode), bar_format="Status GearBox: {desc}")
        self.rpm_bar = tqdm(total=self.car.engine.get_max_rpm(), bar_format="RPM | {bar}{n_fmt} - {total_fmt}")
        self.gear_bar = tqdm(total=self.car.transmission.gear_length(), bar_format="Gear {n_fmt} of {total_fmt}")

    def show(self):
        self.rpm_bar.n = self.car.engine.get_rpm()
        # self.rpm_bar.colour = 'RED' if self.car.status == CarStatus.info_rpm_cutoff else 'WHITE'
        self.gear_bar.n = self.car.transmission.get_gear()
        self.status_bar.desc = transmission_AT_mode.get(self.car.mode)
        self.ref()

    def shutdown(self):
        self.rpm_bar.close()
        self.gear_bar.close()
        self.status_bar.close()
        self.car_info_bar.close()

    def ref(self):
        self.gear_bar.refresh()
        self.rpm_bar.refresh()
        self.status_bar.refresh()
