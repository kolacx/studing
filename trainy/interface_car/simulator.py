import select
import sys
import termios
import tty
from abc import ABC, abstractmethod

from tqdm import tqdm
from cars import Car


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
            print('\n')

    @abstractmethod
    def controls(self, key):
        pass


class SimulatorMT(Simulator):
    def set_gear(self, gear):
        print(f'Set {gear}-gear')

    def quit(self):
        raise Exception('Stop Engine / Exit')

    def controls(self, key):
        if key in ['1', '2', '3', '4', '5', '6']:
            self.set_gear(key)
        elif key == 'q':
            self.quit()


class SimulatorAT(Simulator):
    def __init__(self, car):
        super().__init__(car)
        self.p_mode = False
        self.d_mode = False
        self.n_mode = False
        self.m_mode = False

    def quit(self):
        if self.p_mode:
            raise Exception('Stop Engine / Exit')
        else:
            print(f'Before Exit activate Parking Mode => P <=')

    def up_gear(self):
        self.manual_mode()
        print('Next Gear')

    def down_gear(self):
        self.manual_mode()
        print('Down Gear')

    def manual_mode(self):
        self.p_mode = False
        self.n_mode = False
        self.d_mode = False
        self.m_mode = True

        print(f'Activate Manual Mode => M <=')

    def drive_mode(self):
        self.p_mode = False
        self.n_mode = False
        self.d_mode = True
        self.m_mode = False

        print(f'Activate Drive Mode => D <=')

    def neutral_mode(self):
        self.p_mode = False
        self.d_mode = False
        self.n_mode = True
        self.m_mode = False

        print(f'Activate Neutral Mode => N <=')

    def parking_mode(self):
        self.p_mode = True
        self.d_mode = False
        self.n_mode = False
        self.m_mode = False

        print(f'Activate Neutral Mode => P <=')

    def controls(self, key):
        if key == 'a':
            self.up_gear()
        elif key == 'z':
            self.down_gear()
        elif key == 'n':
            self.neutral_mode()
        elif key == 'd':
            self.drive_mode()
        elif key == 'q':
            self.quit()
        elif key == 'p':
            self.parking_mode()
