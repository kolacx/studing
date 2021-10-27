import select
import sys
import termios
import tty
from abc import ABC, abstractmethod
from typing import Dict

from cars import Car, CarMT, CarAT
from enums import ATGearboxModes

'''

как я реализовал абстрактную симуляцию
и ее взаимоотношения с ее чаилдами


'''


def is_data():
    return select.select([sys.stdin], [], [], 1) == ([sys.stdin], [], [])


class Simulator(ABC):
    def __init__(self, car: Car, controls_map: dict = None):
        self.car = car
        self.controls_map = self.get_ctrl_key()
        if controls_map is not None:
            self.controls_map.update(controls_map)

    @abstractmethod
    def get_ctrl_key(self) -> Dict[str, callable]:
        default_ctrl = {
            "q": self.quit,
            "s": self.start_car,
            "x": self.stop_car
        }

        return default_ctrl

    def drive(self):
        old_settings = termios.tcgetattr(sys.stdin)

        try:
            tty.setcbreak(sys.stdin.fileno())

            while True:
                if is_data():
                    key = sys.stdin.read(1)

                    func = self.controls_map.get(key, None)
                    if func is None:
                        continue

                    try:
                        func(key)
                    except StopIteration as e:
                        print(e)
                        break

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    def quit(self, key):
        raise StopIteration('ABC Stop Engine / Exit')

    def start_car(self, key):
        print('SIMULATOR ABC - start_car')

    def stop_car(self, key):
        print('SIMULATOR ABC - stop_car')


class SimulatorMT(Simulator):
    def __init__(self, car: CarMT):
        super().__init__(car)
        self.car = car

    def get_ctrl_key(self):
        ctrl = super().get_ctrl_key()

        ctrl.update({str(i): self.set_gear for i in range(1, 7)})

        return ctrl

    def set_gear(self, gear):
        print(f'SIMULATOR Set {gear}-gear')
        # self.car.set_gear(gear)


class SimulatorAT(Simulator):
    def __init__(self, car: CarAT):
        super().__init__(car)
        self.mode: ATGearboxModes = ATGearboxModes.parking

    def get_ctrl_key(self):
        ctrl = super().get_ctrl_key()
        ctrl.update({
            "a": self.up_gear,
            "z": self.down_gear,
            "n": self.neutral_mode,
            "d": self.drive_mode,
            "p": self.parking_mode,
            "m": self.manual_mode,
        })

        return ctrl

    def up_gear(self, key):
        if self.mode == ATGearboxModes.manual:
            print('SIMULATOR AT - UP Gear')
        else:
            print('First Activated Manual Mode => press M <==')

    def down_gear(self, key):
        if self.mode == ATGearboxModes.manual:
            print('SIMULATOR AT - Down Gear')
        else:
            print('First Activated Manual Mode => press M <==')

    def manual_mode(self, key):
        self.mode = ATGearboxModes.manual
        print(f'Manual Mode => M <=')

    def drive_mode(self, key):
        self.mode = ATGearboxModes.drive
        print(f'Drive Mode => D <=')

    def neutral_mode(self, key):
        self.mode = ATGearboxModes.neutral
        print(f'Neutral Mode => N <=')

    def parking_mode(self, key):
        self.mode = ATGearboxModes.parking
        print(f'Parking Mode => P <=')


class SimulatorCVT(SimulatorAT):
    pass
