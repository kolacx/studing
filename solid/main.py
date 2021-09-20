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
        return km / self.optimal_speed


class Mercedes(Car):

    def distance(self, km):
        return km / self.optimal_speed


if __name__ == "__main__":

    bmw = BMW('BMW', 110)
    mercedes = Mercedes('Mercedes', 120)
    print(bmw.distance(1000))
    print(mercedes.distance(1000))
