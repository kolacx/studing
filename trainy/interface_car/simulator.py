import select
import sys
import termios
import tty
from abc import ABC, abstractmethod

from tqdm import tqdm
from cars import Car, CarMT, CarAT


def is_data():
    return select.select([sys.stdin], [], [], 1) == ([sys.stdin], [], [])


class Simulator(ABC):
    def __init__(self, car: Car):
        self.car = car

    def drive(self):
        old_settings = termios.tcgetattr(sys.stdin)

        try:
            tty.setcbreak(sys.stdin.fileno())

            while True:
                if is_data():
                    key = sys.stdin.read(1)

                    try:
                        self.controls(key)
                    except Exception as e:
                        print(e)
                        break

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    @abstractmethod
    def controls(self, key):
        pass


class SimulatorMT(Simulator):
    def __init__(self, car: CarMT):
        super().__init__(car)
        self.car = car      # !!!!!!!!!!!!!!!!!!!!!!!!

    def start_engine(self):
        print('SIMULATOR MT - start_engine')
        self.car.start_engine()

    def set_gear(self, gear):
        print(f'SIMULATOR Set {gear}-gear')
        self.car.set_gear(gear)

    def quit(self):
        raise Exception('Stop Engine / Exit')

    def controls(self, key):
        if key in ['1', '2', '3', '4', '5', '6']:
            self.set_gear(key)
        elif key == 'q':
            self.quit()
        elif key == 's':
            self.start_engine()


class SimulatorAT(Simulator):
    def __init__(self, car: CarAT):
        super().__init__(car)
        self.car = car  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.p_mode = False
        self.d_mode = False
        self.n_mode = False
        self.m_mode = False

    def set_mode_permission(self, p_mode=True, d_mode=False, n_mode=False, m_mode=False):
        self.p_mode = p_mode
        self.d_mode = d_mode
        self.n_mode = n_mode
        self.m_mode = m_mode

    def quit(self):
        if self.p_mode:
            raise Exception('Stop Engine / Exit')
        else:
            print(f'Before Exit activate Parking Mode => P <=')

    def start_engine(self):
        print('SIMULATOR AT - start_engine')
        self.car.start_engine()

    def up_gear(self):
        print('SIMULATOR AT - UP Gear')
        self.car.up_gear()

    def down_gear(self):
        print('SIMULATOR AT - DOWN Gear')
        self.car.down_gear()

    def manual_mode(self):
        self.set_mode_permission(m_mode=True)

        print(f'Manual Mode => M <=')

    def drive_mode(self):
        self.set_mode_permission(d_mode=True)

        print(f'Drive Mode => D <=')

    def neutral_mode(self):
        self.set_mode_permission(n_mode=True)

        print(f'Neutral Mode => N <=')

    def parking_mode(self):
        self.set_mode_permission(p_mode=True)

        print(f'Parking Mode => P <=')

    def controls(self, key):
        if key == 'a':
            if self.m_mode:
                self.up_gear()
            else:
                print('First active manual Mode => M <=')
        elif key == 'z':
            if self.m_mode:
                self.down_gear()
            else:
                print('First active manual Mode => M <=')
        elif key == 'n':
            self.neutral_mode()
        elif key == 'd':
            self.drive_mode()
        elif key == 'q':
            self.quit()
        elif key == 'p':
            self.parking_mode()
        elif key == 'm':
            self.manual_mode()
        elif key == 's':
            self.start_engine()


class SimulatorCVT(SimulatorAT):
    pass

