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
    
4) 
    Когда мы устанавливаем Дизельные двигателя в разные автомобили, коефициент мощностми меняется.
'''


class Engine(ABC):
    ROTATION = 3000

    def __init__(self, power_kw):
        self.power_kw = power_kw

    def torque(self, coef=None):
        return (self.power_kw * 9550) / self.ROTATION


class Diesel(Engine):
    def torque(self, coef=1.1):
        return super().torque(coef) * coef


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


class BMW(Car):
    def __init__(self, engine):
        super().__init__('BMW', engine, 1000)


class Audi(Car):
    def __init__(self, engine):
        super().__init__('Audi', engine, 1500)


class Mercedes(Car):
    def __init__(self, engine):
        super().__init__('Mercedes', engine, 2000)
        if isinstance(engine, Diesel):
            self.coef = 1.2

    def average_speed(self):
        return (self.engine.power_kw * self.engine.torque(self.coef)) / self.weight


def calc_distance(dis: Distance, distance: int):
    print(f'Машина {dis.car.brand} проедит {distance}m, за {round(dis.distance(distance), 2)}минут')


def main():

    diesel = Diesel(200)
    benzine = Benzine(250)

    bmw = Distance(BMW(diesel))
    calc_distance(bmw, 1000)
    print(bmw.car.engine.torque())

    audi = Distance(Audi(benzine))
    calc_distance(audi, 2000)
    print(audi.car.engine.torque())

    mercedes = Distance(Mercedes(diesel))
    calc_distance(mercedes, 3000)
    # print(mercedes.car.engine.torque())


if __name__ == "__main__":
    main()
