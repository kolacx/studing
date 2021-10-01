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
                    c = sys.stdin.read(1)

                    if c == 'q':
                        break

                    if c == 's':
                        self.start_engine()

                    self.control(c)

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            print('\n')

    def start_engine(self):
        print('Start Engine')

    @abstractmethod
    def control(self, c):
        pass


class SimulatorMT(Simulator):
    def set_gear(self, gear):
        print(f'Set {gear}-gear')

    def control(self, c):
        if c in ['1', '2', '3', '4', '5', '6']:
            self.set_gear(c)


class SimulatorAT(Simulator):
    def up_gear(self):
        print('Next Gear')

    def down_gear(self):
        print('Down Gear')

    def control(self, c):
        ...