from abc import ABC, abstractmethod

'''
1)
    У нас появляются типы двигателей
    Средняя скорость у разных типов разная.

2)  
    Для каждой машины average_speed разный. 
    Он вычисляется в зависимости Веса втомобиля, Лошадиных сил и крутящиего момента.

3) 
    У дизельнго двигателя крутящий момент на 10 процентов всегда больше.
'''


class Engine(ABC):
    ROTATION = 3000

    def __init__(self, power_kw):
        self.power_kw = power_kw

    def torque(self):
        return (self.power_kw * 9550) / self.ROTATION


class Diesel(Engine):
    def torque(self):
        return super().torque() * 1.1


class Benzine(Engine):
    pass


class Car(ABC):

    def __init__(self, brand, engine: Engine, weight):
        self.brand = brand
        self.weight = weight
        self.engine = engine

    def average_speed(self):
        return (self.engine.power_kw * self.engine.torque()) / self.weight


class Distance:
    def __init__(self, car: Car):
        self.car = car

    def distance(self, km):
        return (km / self.car.average_speed()) * 60


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

    d = Diesel(200)
    b = Benzine(250)

    bmw310 = Distance(BMW310(d))
    calc_distance(bmw310, 1000)

    bmw320 = Distance(BMW320(b))
    calc_distance(bmw320, 2000)

    bmw330 = Distance(BMW330(d))
    calc_distance(bmw330, 3000)

    bmw340 = Distance(BMW340(b))
    calc_distance(bmw340, 4000)

    bmw350 = Distance(BMW350(b))
    calc_distance(bmw350, 5000)


if __name__ == "__main__":
    main()
