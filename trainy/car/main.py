from abc import ABC, abstractmethod

'''
    У нас появляются типы двигателей
    Средняя скорость у разных типов разная.
'''


class Engine(ABC):
    def __init__(self, optimal_speed):
        self.optimal_speed = optimal_speed


class Diesel(Engine):
    pass


class Benzine(Engine):
    pass


class Car(ABC):

    def __init__(self, brand, engine: Engine):
        self.brand = brand
        self.engine = engine


class Distance:
    def __init__(self, car: Car):
        self.car = car

    def distance(self, km):
        return (km / self.car.engine.optimal_speed) * 60


class BMW310(Car):
    def __init__(self, engine):
        super().__init__('BMW310', engine)


class BMW320(Car):
    def __init__(self, engine):
        super().__init__('BMW320', engine)


class BMW330(Car):
    def __init__(self, engine):
        super().__init__('BMW330', engine)


class BMW340(Car):
    def __init__(self, engine):
        super().__init__('BMW340', engine)


class BMW350(Car):
    def __init__(self, engine):
        super().__init__('BMW350', engine)


def calc_distance(dis: Distance, distance: int):
    print(f'Машина {dis.car.brand} проедит {distance}m, за {round(dis.distance(distance), 2)}минут')


def main():

    d = Diesel(123)
    b = Benzine(321)

    bmw310 = Distance(BMW310(d))
    calc_distance(bmw310, 1000)

    bmw320 = Distance(BMW320(b))
    calc_distance(bmw320, 2000)

    bmw330 = Distance(BMW330(d))
    calc_distance(bmw330, 3000)

    bmw340 = Distance(BMW340(b))
    calc_distance(bmw340, 4000)

    bmw350 = Distance(BMW350(d))
    calc_distance(bmw350, 5000)


if __name__ == "__main__":
    main()
