from cars import CarMT, CarAT
from simulator import SimulatorMT, SimulatorAT
from engines import Engine
from transmissions import MT, AT

'''
Simulatro MT
    Не нравится что q == quit
    НАслетоватся от Simulator MT и сделать так чтобы quit был равен - ?
    
    Есть Какойто питоновский вариант.
    
    Пытаюсь описать остоя ние Н переменными.
    Описывать какето состояние Н переменными.
    
    Состояние ЕНум.
'''


def quit():
    raise Exception('Stop Engine / Exit')


def start_engine():
    print('SIMULATOR AT - start_engine')


def up_gear():
    print('SIMULATOR AT - UP Gear')


def down_gear():
    print('SIMULATOR AT - DOWN Gear')


def manual_mode():
    print(f'Manual Mode => M <=')


def drive_mode():
    print(f'Drive Mode => D <=')


def neutral_mode():
    print(f'Neutral Mode => N <=')


def parking_mode():
    print(f'Parking Mode => P <=')


f_at = {
    "a": up_gear,
    "z": down_gear,
    "n": neutral_mode,
    "d": drive_mode,
    "q": quit,
    "p": parking_mode,
    "m": manual_mode,
    "s": start_engine,
}


f_mt = {
    "q": quit,
    "s": start_engine
}


class Smt(SimulatorMT):
    def __init__(self, car, controls):
        super().__init__(car, controls)

    def get_controls(self, control_map):
        control_map["r"] = self.quit
        control_map["e"] = control_map.pop("q")
        return control_map


if __name__ == "__main__":
    print("GOs")

    mt = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83])
    at = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1])
    engine = Engine(6500)
    car_mt = CarMT(engine, mt)
    car_at = CarAT(engine, at)

    choise = input('Select Transmission: \n 1 - MT, 2-AT \n')

    car = Smt(car_mt, f_mt) if choise == "1" else SimulatorAT(car_at, f)

    print(f'You at {car.car.transmission.__class__}')

    car.drive()
