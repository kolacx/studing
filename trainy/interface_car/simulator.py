import select
import sys
import termios
import tty

from tqdm import tqdm
from cars import Car


def is_data():
    return select.select([sys.stdin], [], [], 1) == ([sys.stdin], [], [])


'''
Что делает симулятор.

Что мы можем сделать в симуляторе:
Завести машину
разогнатся
затормозить
переключить передачу

Какую информациб предоставляет нам симулятор
    Текущую скорость
    Максимальную скорость
    текущую передачу
    заведена ли машина
    Обороты двигателя
'''


class Simulator:
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
        print(f"Engine On/Off: On \t"
              f"Current Speed: current_speed \t"
              f"Current Gear: 0000 \t"
              f"RPM: rpm - maxRPM - 000", end="\r")

    def start_engine(self):
        print('\n start_engine')

    def switch_gear(self, gear):
        print(f'\n switch_gear {gear}')

    def rpm_up(self):
        print('\n rpm_up +100')

    def rpm_down(self):
        print('\n rpm_up -100')