# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

from cars import CarMT, CarAT, Car
from simulator import SimulatorMT, SimulatorAT, Simulator
from engines import Engine
from transmissions import MT, AT, GearBox
from display import DisplayMT, DisplayAT, bcolors, Display

'''
План капкан.

1) Добавить Симуляцию автоматической коробки передач.
    
реализовать набор сброс скорости
переключение передач
подсброс оборотов при переключении
Показать скрость.

То что относится к нашей машине в диапазоне нашего контекста. К чему имеет оно отношение. 
К Кару, Двигателю или трансмиссии.

Не выходя за рамки нашего контекст взять часть автомобиля, 
и понять к чему она относится, и почему.


Прояснить для себя что такое контекст моей задачи.
Влияет ли наша задача на наш контекст


Точка принятия решения.
Она показывает для чего вообще это было реализованно.
Старт в котором есть IF
Есть в разрабатыванной сущности чтото что может повлиять на основное поведение. 
Задать ему условия.



Информация о машине общая
Сделать диапазон переключение передча для разных коробок

'''

mt1 = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83], 'MT ZF 1')
mt2 = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83], 'MT ZF 2')
mt3 = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83], 'MT ZF 3')
mt4 = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83], 'MT ZF 4')
mt5 = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83], 'MT ZF 5')

at1 = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1], 'AT FE 1')
at2 = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1], 'AT FE 2')
at3 = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1], 'AT FE 3')
at4 = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1], 'AT FE 4')
at5 = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1], 'AT FE 5')

engine1 = Engine(5500)
engine2 = Engine(6500)
engine3 = Engine(7500)
engine4 = Engine(8500)
engine5 = Engine(9500)

nissan = CarMT(engine1, mt1, 'Nissan')
porsche = CarMT(engine2, mt2, 'Porsche')
audi = CarMT(engine3, mt3, 'Audi')
hyuinday = CarMT(engine4, mt4, 'Hyuinday')
ford = CarMT(engine5, mt5, 'Ford')
volkswagen = CarAT(engine1, at1, 'Volkswagen')
honda = CarAT(engine2, at2, 'Honda')
bmw = CarAT(engine3, at3, 'BMW')
mercedes = CarAT(engine4, at4, 'Mercedes')
toyota = CarAT(engine5, at5, 'Toyota')


cars_dict = {
    "1": nissan,
    "2": porsche,
    "3": audi,
    "4": hyuinday,
    "5": ford,
    "6": volkswagen,
    "7": honda,
    "8": bmw,
    "9": mercedes,
    "10": toyota,
}

# ========= Work with CAR =========


class CarBuilder(ABC):
    @abstractmethod
    def set_engine(self, engine: Engine):
        pass

    @abstractmethod
    def set_transmission(self, transmission: GearBox):
        pass

    @abstractmethod
    def set_name(self, name: str):
        pass

    @abstractmethod
    def build(self):
        pass


class CarMTBuilder(CarBuilder):

    def set_engine(self, engine: Engine):
        self.engine = engine
        return self

    def set_transmission(self, transmission: MT):
        self.transmission = transmission
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def build(self) -> CarMT:
        return CarMT(self.engine, self.transmission, self.name)


class CarATBuilder(CarBuilder):

    def set_engine(self, engine: Engine):
        self.engine = engine
        return self

    def set_transmission(self, transmission: AT):
        self.transmission = transmission
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def build(self) -> CarAT:
        return CarAT(self.engine, self.transmission, self.name)


class CarFactory(ABC):
    @abstractmethod
    def get_car(self, engine, transmission, name) -> Car:
        pass


class CarMTFactory(CarFactory):
    def get_car(self, engine, transmission, name) -> CarMT:
        return CarMTBuilder().set_engine(engine).set_transmission(transmission).set_name(name).build()


class CarATFactory(CarFactory):
    def get_car(self, engine, transmission, name) -> CarAT:
        return CarATBuilder().set_engine(engine).set_transmission(transmission).set_name(name).build()


# ========= Work with SIMULATOR =========


class SimulatorBuilder(ABC):

    @abstractmethod
    def set_car(self, car: Car):
        pass

    @abstractmethod
    def set_display(self, display):
        pass

    @abstractmethod
    def build(self) -> Simulator:
        pass


class SimulatorMTBuilder(SimulatorBuilder):

    def set_car(self, car: CarMT):
        self.car = car
        return self

    def set_display(self, display):
        self.display = display
        return self

    def build(self) -> SimulatorMT:
        return SimulatorMT(self.car, self.display)


class SimulatorATBuilder(SimulatorBuilder):

    def set_car(self, car: CarAT):
        self.car = car
        return self

    def set_display(self, display):
        self.display = display
        return self

    def build(self) -> SimulatorAT:
        return SimulatorAT(self.car, self.display)


class SimulatorFactory(ABC):
    @abstractmethod
    def get_simulator(self, car: Car, display: Display) -> Simulator:
        pass


class SimulatorMTFactory(SimulatorFactory):
    def get_simulator(self, car: CarMT, display: DisplayMT) -> SimulatorMT:
        return SimulatorMTBuilder().set_car(car).set_display(display).build()


class SimulatorATFactory(SimulatorFactory):
    def get_simulator(self, car: CarAT, display: DisplayAT) -> SimulatorAT:
        return SimulatorATBuilder().set_car(car).set_display(display).build()


# ========= Work with DISPLAY =========


class DisplayBuilder(ABC):
    @abstractmethod
    def set_car(self, car: Car):
        pass

    @abstractmethod
    def build(self):
        pass


class DisplayMTBuilder(DisplayBuilder):
    def set_car(self, car: CarMT):
        self.car = car
        return self

    def build(self) -> DisplayMT:
        return DisplayMT(self.car)


class DisplayATBuilder(DisplayBuilder):
    def set_car(self, car: CarAT):
        self.car = car
        return self

    def build(self) -> DisplayAT:
        return DisplayAT(self.car)


class DisplayFactory(ABC):
    @abstractmethod
    def get_display(self, car: Car) -> Display:
        pass


class DisplayMTFactory(DisplayFactory):
    def get_display(self, car: CarMT) -> DisplayMT:
        return DisplayMTBuilder().set_car(car).build()


class DisplayATFactory(DisplayFactory):
    def get_display(self, car: CarAT) -> DisplayAT:
        return DisplayATBuilder().set_car(car).build()


def client(simulator: Simulator):
    simulator.print_ctrl()
    simulator.drive()


if __name__ == "__main__":

    car = CarMTFactory().get_car(engine1, mt1, 'Xyiita')
    display = DisplayMTFactory().get_display(car)
    simulator = SimulatorMTFactory().get_simulator(car, display)

    client(simulator)








    # print('\n')
    # welcome_message = bcolors.HEADER + '\U0001F308 \U0001F917 Welcome in owers  RCC (Rent Car Centers) \U0001F917 \U0001F308' + bcolors.ENDC
    # print(welcome_message.center(120) + '\n')
    #
    # for k, v in cars_dict.items():
    #     print(f'{bcolors.UNDERLINE}{k}{bcolors.ENDC} \U0001F698 {v}')
    #
    # print('\n')
    #
    # choise = input(bcolors.UNDERLINE + 'Choise Car For Rent ->> # ' + bcolors.ENDC)
    # car = cars_dict.get(choise)
    #
    # print(f'Yours choise \U0001F449 {car}. \U0001F91F')
    #
    # if type(car.transmission) == MT:
    #     display = DisplayForMyCar(car)
    #     simulator = SimulatorMT(car, display)
    #     print_ctrl(simulator.get_ctrl_key())
    #     simulator.drive()
    #
    # elif type(car.transmission) == AT:
    #     display = DisplayForMyCarAT(car)
    #     simulator = SimulatorAT(car, display)
    #     print_ctrl(simulator.get_ctrl_key())
    #     simulator.drive()
#