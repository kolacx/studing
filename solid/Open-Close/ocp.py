from abc import ABC, abstractmethod


class A(ABC):
    def __init__(self, car):
        self.car = car

    @abstractmethod
    def check_brand(self):
        return False if self.car.brand != "UAZ" else True


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class IfBmw(A):

    def check_brand(self):
        return False if self.car.brand != "BMW" else True


class IfMercedes(A):

    def check_brand(self):
        return False if self.car.brand != "Mercedes" else True


if __name__ == "__main__":
    print('*********')

    car = Car("BMW", 5)
    b = IfBmw(car)
    m = IfMercedes(car)

    print(b.check_brand())
    print(m.check_brand())
