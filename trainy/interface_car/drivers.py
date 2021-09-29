import select
import sys
import termios
import tty

from tqdm import tqdm
from cars import Car


def is_data():
    return select.select([sys.stdin], [], [], 1) == ([sys.stdin], [], [])


class Driver:
    def __init__(self, car: Car):
        self.car = car
        self.rpm = tqdm(total=car.engine.max_rpm)

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

                    if c == 'u':
                        self.rpm.update(100)

                    if c == 'd':
                        self.rpm.update(-100)

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            self.rpm.close()

    def display(self, rpm):
        self.rpm.update(rpm)

    def start_engine(self):
        self.car.engine.rpm = 800
        self.display(rpm=800)

    def stop_engine(self):
        self.car.engine.rpm = 0
        self.display(rpm=0)
