from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand, optimal_speed):
        self.brand = brand
        self.optimal_speed = optimal_speed

    @abstractmethod
    def distance(self, km):
        ...


class BMW(Car):

    def distance(self, km):
        return (km / self.optimal_speed) * 60


class Mercedes(Car):

    def distance(self, km):
        return (km / self.optimal_speed) * 60


class BMW310(Car):
    def __init__(self):
        super().__init__('BMW310', 110)

    def distance(self, km):
        return (km / self.optimal_speed) * 60


class BMW320(Car):
    def __init__(self):
        super().__init__('BMW320', 120)

    def distance(self, km):
        return (km / self.optimal_speed) * 60


class BMW330(Car):
    def __init__(self):
        super().__init__('BMW330', 130)

    def distance(self, km):
        return (km / self.optimal_speed) * 60


class BMW340(Car):
    def __init__(self):
        super().__init__('BMW340', 140)

    def distance(self, km):
        return (km / self.optimal_speed) * 60


class BMW350(Car):
    def __init__(self):
        super().__init__('BMW350', 150)

    def distance(self, km):
        return (km / self.optimal_speed) * 60


def calc_distance(car: Car, distance: int):
    print(f'Машина {car.brand} проедит {distance}m, за {round(car.distance(distance), 2)}минут')


def main():
    bmw = BMW('BMW', 110)
    mercedes = Mercedes('Mercedes', 120)
    print(bmw.distance(1000))
    print(mercedes.distance(1000))

    bmw310 = BMW310()
    calc_distance(bmw310, 1000)

    bmw320 = BMW320()
    calc_distance(bmw320, 2000)

    bmw330 = BMW330()
    calc_distance(bmw330, 3000)

    bmw340 = BMW340()
    calc_distance(bmw340, 4000)

    bmw350 = BMW350()
    calc_distance(bmw350, 5000)

if __name__ == "__main__":
    main()
