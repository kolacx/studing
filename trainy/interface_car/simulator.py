import select
import sys
import termios
import tty

from tqdm import tqdm
from cars import Car


def is_data():
    return select.select([sys.stdin], [], [], 1) == ([sys.stdin], [], [])


class SimulatorMT:
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

                    if c in [str(i + 1) for i in range(self.car.transmission.get_len_gearbox())]:
                        self.switch_gear(c)

                    if c == 's':
                        self.start_engine()

                    if c == 'a':
                        self.rpm_up()

                    if c == 'z':
                        self.rpm_down()

                self.display()

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            print('\n')

    def display(self):
        print(f"Engine On/Off: {'On' if self.car.engine.rpm > 0 else 'Off'} \t"
              f"Current Speed: {self.current_speed()} \t"
              f"Current Gear: {self.car.get_current_gear()} \t"
              f"RPM: {self.car.engine.rpm} - maxRPM - {self.car.engine.max_rpm}", end="\r")

    def start_engine(self):
        self.car.start_engine()

    def switch_gear(self, gear):
        self.car.switch_gear(gear)

    def rpm_up(self):
        self.car.rpm_up()

    def rpm_down(self):
        self.car.rpm_down()

    def current_speed(self):
        return self.car.current_speed()


class SimulatorAT:
    def __init__(self, car: Car):
        self.car = car
        self.transmission_mode = 'p'

    def drive(self):
        old_settings = termios.tcgetattr(sys.stdin)

        try:
            tty.setcbreak(sys.stdin.fileno())

            while True:
                if is_data():
                    c = sys.stdin.read(1)

                    if c == 'q':
                        break

                    if c == 'p':
                        pass

                    if c == 'r':
                        pass

                    if c == 'n':
                        pass

                    if c == 'd':
                        self.transmission_mode = c
                        self.switch_gear(1)

                    if c == 's':
                        self.start_engine()

                    if c == 'a':
                        self.rpm_up()

                    if c == 'z':
                        self.rpm_down()

                if self.transmission_mode == 'd':
                    self.drive_mode()

                self.display()

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            print('\n')

    def display(self):
        print(f"Engine On/Off: {'On' if self.car.engine.rpm >= 0.0 else 'Off'} \t"
              f"Current Speed: {self.car.current_speed()} \t"
              f"Current Gear: {self.car.get_current_gear()} \t"
              f"RPM: {self.car.engine.rpm} - maxRPM - {self.car.engine.max_rpm}", end="\r")

    def drive_mode(self):
        if self.car.current_speed() < 20:
            self.switch_gear(1)
        elif self.car.current_speed() < 40:
            self.switch_gear(2)
        elif self.car.current_speed() < 60:
            self.switch_gear(3)
        elif self.car.current_speed() < 80:
            self.switch_gear(4)
        elif self.car.current_speed() < 100:
            self.switch_gear(5)
        elif self.car.current_speed() < 120:
            self.switch_gear(6)

    def start_engine(self):
        self.car.start_engine()

    def switch_gear(self, gear):
        self.car.switch_gear(gear)

    def current_gear(self):
        return self.car.get_current_gear()

    def rpm_up(self):
        self.car.rpm_up()

    def rpm_down(self):
        self.car.rpm_down()

    def current_speed(self):
        return self.car.current_speed()
