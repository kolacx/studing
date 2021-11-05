from cars import CarMT, CarAT
from simulator import SimulatorMT, SimulatorAT
from engines import Engine
from transmissions import MT, AT
from display import DisplayForMyCar

'''
План капкан.

1) Добавить Симуляцию автоматической коробки передач.
    
    
'''


if __name__ == "__main__":
    print("GOs")

    mt = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83])
    at = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1])

    engine = Engine(6500)

    car_mt = CarMT(engine, mt)
    car_at = CarAT(engine, at)

    choise = input('Select Transmission: \n 1 - MT, 2-AT \n')

    car = car_mt if choise == "1" else car_at

    display = DisplayForMyCar(car)

    simulator = SimulatorMT(car, display) if choise == "1" else SimulatorAT(car, display)
    simulator.drive()



