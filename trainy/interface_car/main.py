from cars import CarMT, CarAT
from simulator import SimulatorMT, SimulatorAT
from engines import Engine
from transmissions import MT, AT
from display import DisplayForMyCar, DisplayForMyCarAT

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
'''


if __name__ == "__main__":
    print("GOs")

    mt = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83])
    at = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1])

    engine = Engine(6500)

    car_mt = CarMT(engine, mt)
    car_at = CarAT(engine, at)

    choise = input('Select Transmission: \n 1 - MT, 2-AT \n')

    display = DisplayForMyCar(car_mt) if choise == '1' else DisplayForMyCarAT(car_at)

    simulator = SimulatorMT(car_mt, display) if choise == '1' else SimulatorAT(car_at, display)
    simulator.drive()



