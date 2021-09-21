from abc import ABC, abstractmethod

'''
1)
    У нас появляются типы двигателей
    Средняя скорость у разных типов разная.

2)  
    Для каждой машины average_speed разный. 
    Он вычисляется в зависимости Веса втомобиля, Лошадиных сил и крутящиего момента.
    
'''


class Engine(ABC):
    def __init__(self, horse_power, torque):
        self.horse_power = horse_power
        self.torque = torque


class Diesel(Engine):
    pass


class Benzine(Engine):
    pass


class Car(ABC):

    def __init__(self, brand, engine: Engine, weight):
        self.brand = brand
        self.weight = weight
        self.engine = engine
        self.average_speed = self.average_speed()

    def average_speed(self):
        return (self.engine.horse_power * self.engine.torque) / self.weight


class Distance:
    def __init__(self, car: Car):
        self.car = car

    def distance(self, km):
        return (km / self.car.average_speed) * 60


class BMW310(Car):
    def __init__(self, engine):
        super().__init__('BMW310', engine, 1000)


class BMW320(Car):
    def __init__(self, engine):
        super().__init__('BMW320', engine, 1200)


class BMW330(Car):
    def __init__(self, engine):
        super().__init__('BMW330', engine, 1500)


class BMW340(Car):
    def __init__(self, engine):
        super().__init__('BMW340', engine, 1700)


class BMW350(Car):
    def __init__(self, engine):
        super().__init__('BMW350', engine, 2000)


def calc_distance(dis: Distance, distance: int):
    print(f'Машина {dis.car.brand} проедит {distance}m, за {round(dis.distance(distance), 2)}минут')


def main():

    d = Diesel(200, 350)
    b = Benzine(250, 300)

    bmw310 = Distance(BMW310(d))
    calc_distance(bmw310, 1000)
    print(bmw310.car.average_speed)

    bmw320 = Distance(BMW320(b))
    calc_distance(bmw320, 2000)
    print(bmw320.car.average_speed)

    bmw330 = Distance(BMW330(d))
    calc_distance(bmw330, 3000)
    print(bmw330.car.average_speed)

    bmw340 = Distance(BMW340(b))
    calc_distance(bmw340, 4000)
    print(bmw340.car.average_speed)

    bmw350 = Distance(BMW350(b))
    calc_distance(bmw350, 5000)
    print(bmw350.car.average_speed)


if __name__ == "__main__":
    main()
