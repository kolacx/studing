from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand, optimal_speed):
        self.brand = brand
        self.optimal_speed = optimal_speed


class Distance:
    def __init__(self, car):
        self.car = car

    def distance(self, km):
        return (km / self.car.optimal_speed) * 60


class BMW310(Car):
    def __init__(self):
        super().__init__('BMW310', 110)


class BMW320(Car):
    def __init__(self):
        super().__init__('BMW320', 120)


class BMW330(Car):
    def __init__(self):
        super().__init__('BMW330', 130)


class BMW340(Car):
    def __init__(self):
        super().__init__('BMW340', 140)


class BMW350(Car):
    def __init__(self):
        super().__init__('BMW350', 150)


def calc_distance(dis: Distance, distance: int):
    print(f'Машина {dis.car.brand} проедит {distance}m, за {round(dis.distance(distance), 2)}минут')


def main():
    # bmw = BMW('BMW', 110)
    # mercedes = Mercedes('Mercedes', 120)
    # print(bmw.distance(1000))
    # print(mercedes.distance(1000))

    bmw310 = Distance(BMW310())
    calc_distance(bmw310, 1000)

    bmw320 = Distance(BMW320())
    calc_distance(bmw320, 2000)

    bmw330 = Distance(BMW330())
    calc_distance(bmw330, 3000)

    bmw340 = Distance(BMW340())
    calc_distance(bmw340, 4000)

    bmw350 = Distance(BMW350())
    calc_distance(bmw350, 5000)


if __name__ == "__main__":
    main()
