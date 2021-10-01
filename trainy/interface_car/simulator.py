import select
import sys
import termios
import tty
from abc import ABC

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

                    if c == 'a':
                        self.gear_up()

                    if c == 'z':
                        self.gear_down()

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            print('\n')

    def start_engine(self):
        print('Start Engine')

    def gear_up(self):
        print('Gear Up')

    def gear_down(self):
        print('Gear Down')


class SimulatorMT(Simulator):
    pass