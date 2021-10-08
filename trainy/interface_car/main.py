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


class Smt(SimulatorMT):

    def get_ctrl_key(self):
        c = super().get_ctrl_key()
        c.update({"e": self.qqq})
        return c

    def qqq(self):
        raise Exception('eeee')


if __name__ == "__main__":
    print("GOs")

    mt = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83])
    at = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1])
    engine = Engine(6500)
    car_mt = CarMT(engine, mt)
    car_at = CarAT(engine, at)

    choise = input('Select Transmission: \n 1 - MT, 2-AT \n')

    car = SimulatorMT(car_mt) if choise == "1" else SimulatorAT(car_at)

    print(f'You at {car.car.transmission.__class__}')

    car.drive()

    # s = SimulatorAT(car_at)
    #
    # s.mode = 1