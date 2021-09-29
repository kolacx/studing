import sys
import select
import tty
import termios
from abc import ABC, abstractmethod

from tqdm import tqdm

'''
    max_speed = 
    current_speed =
    rpm =
    gear = 
    

    Обобщение задачи.
    Построить симулятор управления машиной.
    
    Он должен уметь следующее:
        1) Иметь информационную составляющую
        2) Органы управления машиной.
        
    Информационная составляющая:
        1) Максимальная скорость ( Статическое значение )
        2) Текущая скорость (Динамическое значение, высчитывается в зависимости от оборотов и передаточного числа)
        3) Обороты двигателя (Динамическое значение. Устанавливает пользователь во время пользования)
        4) Текущая передача (Может быть динамическим либо статическим, так как мы заведомо знаем о существованиее 
            2х типов коробок передач МТ и АКПП)
        5) Состояние машины (Заведена / Остановлена)
        
    Органы управления:
        1) Набор оборотов
        2) Переключатель передач
        3) Кнопка запуска / Остановки автомобиля
        
    Машина
        Машина состоит из 2х сущностей Двигателя и Коробки передач.
        Свойства Двигателя:
            Обороты
            Максимальные обороты
            
        Коробка передач:
        Свойства коробки передач МТ:
            Передаточное число
            Список передач
            
        Свойсвтва коробки передач АКПП:
            Передаточное число
            Список передач
    
        Разница коробок в их управлении.
            В ручной коробке мы самостоятельно выбераем передачу,
            В автоматической это решает комп.    
            
'''


class Engine:
    def __init__(self, max_rpm: int):
        self.rpm = 0
        self.max_rpm = max_rpm


class GearBox(ABC):
    def __init__(self):
        self.ratio = 0

    def conver_to_speed(self, rpm):
        return (rpm * self.ratio) / 1000

    @abstractmethod
    def shift(self, gear):
        pass


class Car:
    def __init__(self, engine: Engine, gear_box: GearBox, max_speed: int):
        self.engine = engine
        self.gear_box = gear_box
        self.max_speed = max_speed


class MT(GearBox):
    def __init__(self, ratio_list):
        self.ratio_list = ratio_list
        super().__init__()

    def shift(self, gear):
        self.ratio = self.ratio_list[gear - 1]


class AT(MT):
    pass


mt = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83])
at = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1])

engine = Engine(7500)

car = Car(engine, mt, 250)
car2 = Car(engine, at, 220)


def isData():
    return select.select([sys.stdin], [], [], 1) == ([sys.stdin], [], [])


old_settings = termios.tcgetattr(sys.stdin)

print('Select Car: MT - 1, AT - 2')
key = sys.stdin.read(1)
if key == "1":
    car = Car(engine, mt, 250)
elif key == "2":
    car = Car(engine, at, 220)

print('Max_Speed - ', car.max_speed)
current_speed = tqdm(desc='Current_speed', total=car.max_speed)
rpm = tqdm(desc='RPM', total=car.engine.max_rpm)
gear = tqdm()

try:
    tty.setcbreak(sys.stdin.fileno())

    i = 0
    while True:
        i += 1

        if isData():
            c = sys.stdin.read(1)

            if c == 'q':         # x1b is ESC
                break

            if c == 'w':
                car.gear_box.ratio = car.gear_box.ratio_list[1]

            if c == 'u':
                if car.gear_box.ratio == 0:
                    new_rpm = car.engine.rpm + 200

                    if new_rpm >= car.engine.max_rpm:
                        rpm.update(-500)
                        car.engine.rpm -= 500
                    else:
                        car.engine.rpm = new_rpm
                        rpm.update(200)
                else:
                    new_rpm = car.engine.rpm + 200

                    if new_rpm >= car.engine.max_rpm:
                        rpm.update(-500)
                        car.engine.rpm -= 500
                        current_speed.update(-100)
                    else:
                        car.engine.rpm = new_rpm
                        rpm.update(200)

                        speed = car.gear_box.conver_to_speed(new_rpm)

                        current_speed.update(speed)

finally:
    # max_speed.close()
    current_speed.close()
    rpm.close()
    gear.close()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
