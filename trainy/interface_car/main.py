# -*- coding: utf-8 -*-
from cars import CarMT, CarAT, Car
from engines import Engine
from factorys import CarCatalog, AbcSimulator, SimulatorATFactory
from simulator import SimulatorMT, SimulatorAT, Simulator
from transmissions import MT, AT
from display import DisplayMT, DisplayAT, bcolors, Display

from loaders import ListLoader, LoadFromCSV, LoadFromJSON, LoadFromXML, LoadFromYAML


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

mt1 = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83], 'MTZF1')
mt2 = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83], 'MTZF2')
mt3 = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83], 'MTZF3')
mt4 = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83], 'MTZF4')
mt5 = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83], 'MTZF5')

at1 = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1], 'ATFE1')
at2 = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1], 'ATFE2')
at3 = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1], 'ATFE3')
at4 = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1], 'ATFE4')
at5 = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1], 'ATFE5')

engine1 = Engine(5500, 750)
engine2 = Engine(6500, 750)
engine3 = Engine(7500, 750)
engine4 = Engine(8500, 750)
engine5 = Engine(9500, 750)

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

'''
Соглашение при создании машины.
    У нас есть соглашение абривиатуры автомобиля.
    bmw_{MAX-RPM-ENGINE}_{NAME-TRANSMISSION}
    bmw_7500_zf5hp24
    
    Ета абривиатура для того чтобы мы могливыдать свои автомобили.


Если мы создаем новую машину.
    Нам нужно передать пихло трансмиссию и модель машины

'''


if __name__ == "__main__":
    print('\n')
    welcome_message = bcolors.HEADER + '\U0001F308 \U0001F917 Welcome in owers  RCC (Rent Car Centers) \U0001F917 \U0001F308' + bcolors.ENDC
    print(welcome_message.center(120) + '\n')

    for k, v in cars_dict.items():
        print(f'{bcolors.UNDERLINE}{k}{bcolors.ENDC} \U0001F698 {v}')

    print('\n')

    choise = input(bcolors.UNDERLINE + 'Choise Car For Rent ->> # ' + bcolors.ENDC)
    car = cars_dict.get(choise)

    print(f'Yours choise \U0001F449 {car}. \U0001F91F')

    if type(car.transmission) == MT:
        display = DisplayMT(car)
        simulator = SimulatorMT(car, display)
        print(simulator.get_ctrl_key())
        simulator.drive()

    elif type(car.transmission) == AT:
        display = DisplayAT(car)
        simulator = SimulatorAT(car, display)
        print(simulator.get_ctrl_key())
        simulator.drive()
