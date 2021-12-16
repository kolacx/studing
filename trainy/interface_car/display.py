from abc import ABC, abstractmethod
from typing import Optional, Union

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


class Display(ABC):
    car: Union[CarMT, CarAT, Car]

    def __init__(self, car: Car):
        self.car = car

        self.car_info_bar = tqdm(desc=f"{self.car}", bar_format="You at: {desc}")
        self.rpm_bar = tqdm(total=self.car.engine.get_max_rpm(), bar_format="RPM | {bar}{n_fmt} - {total_fmt}")
        self.speed = tqdm(desc='Speed', total=400, bar_format="{desc}: {n_fmt}")
        self.gear_bar = tqdm(total=self.car.transmission.gear_length(), bar_format="Gear {n_fmt} of {total_fmt}")

    def show(self):
        cur_rpm = self.car.engine.get_rpm()

        self.rpm_bar.n = cur_rpm
        self.speed.n = int(self.current_speed(cur_rpm))
        self.gear_bar.n = self.car.transmission.get_gear()

        self.ref()

    def shutdown(self):
        self.rpm_bar.close()
        self.speed.close()
        self.gear_bar.close()
        self.car_info_bar.close()

    def ref(self):
        self.speed.refresh()
        self.gear_bar.refresh()
        self.rpm_bar.refresh()

    def current_speed(self, rpm):
        if self.car.transmission.get_gear() == 0:
            return 0

        r_cm = (self.car.wheel.radius * 2.54) * 10
        profile_height = self.car.wheel.tire.width * (self.car.wheel.tire.height / 100)
        w_h = (profile_height * 2 + r_cm) / 10

        speed = rpm * (w_h / ((3.64 * self.car.transmission.get_ratio()) * 530.616))

        return speed


class DisplayMT(Display):

    def __init__(self, car: CarMT):
        super().__init__(car)


transmission_AT_mode = {
    ATGearboxModes.neutral: 'Neutral',
    ATGearboxModes.parking: 'Parking',
    ATGearboxModes.drive: 'Drive',
    ATGearboxModes.reverse: 'Revers',
    ATGearboxModes.manual: 'Manual'
}


class DisplayAT(Display):

    def __init__(self, car: CarAT):
        super().__init__(car)
        self.status_bar = tqdm(desc=transmission_AT_mode.get(self.car.mode), bar_format="Status GearBox: {desc}")

    def show(self):
        super().show()
        self.status_bar.desc = transmission_AT_mode.get(self.car.mode)
        self.ref()

    def shutdown(self):
        super().shutdown()
        self.status_bar.close()

    def ref(self):
        super().ref()
        self.status_bar.refresh()
