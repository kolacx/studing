import select
import sys
import termios
import tty

from tqdm import tqdm
from cars import Car
from transmissions import MT


def is_data():
    return select.select([sys.stdin], [], [], 1) == ([sys.stdin], [], [])


class Driver:
    def __init__(self, car: Car, ctrl):
        self.car = car
        self.rpm = tqdm(total=car.engine.max_rpm)
        self.ctrl = ctrl

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
                        if self.car.engine.rpm == 0:
                            self.start_engine()

                    if c == 'x':
                        if self.car.engine.rpm != 0:
                            self.stop_engine()

                    self.ctrl.do(c)

                    self.display(rpm=self.car.engine.rpm)

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            self.rpm.close()

    def display(self, rpm):
        self.rpm.update(rpm)

    def start_engine(self):
        self.car.engine.rpm = 800

    def stop_engine(self):
        self.car.engine.rpm = 0


class ControlMT:
    def __init__(self, transmission: MT):
        self.mt = transmission

    def set_gear(self, gear):
        self.mt.set_gear(gear)

    def do(self, c):
        if c == 'a':
            self.set_gear(1)
