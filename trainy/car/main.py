from abc import ABC, abstractmethod
from cars import Car, Distance
from engine import Diesel, Benzine

'''
1)
    У нас появляются типы двигателей
    Средняя скорость у разных типов разная.

2)  
    Для каждой машины average_speed разный. 
    Он вычисляется в зависимости Веса втомобиля, Лошадиных сил и крутящиего момента.

3) 
    У дизельнго двигателя крутящий момент на 10 процентов всегда больше.
    
========================================
4) 
    Когда мы устанавливаем Дизельные двигателя в разные автомобили, коефициент мощностми меняется.
    
5) 
    Все машины должны проезжать одно и тоже растояние. +
    подогнать цифры так чтобы бмв проезжало за 10 минут. +
'''


class BMW(Car):
    def __init__(self, engine):
        super().__init__('BMW', engine, 1000)


class Audi(Car):
    def __init__(self, engine):
        super().__init__('Audi', engine, 1500)


class Mercedes(Car):
    def __init__(self, engine):
        super().__init__('Mercedes', engine, 1000, coef=1.2)


def calc_distance(dis: Distance, distance: int):
    print(f'Машина {dis.car.brand} проедит {distance}m, за {round(dis.distance(distance), 2)} минут')


def main():

    diesel = Diesel(185.12)
    benzine = Benzine(250.65)

    DISTANCE = 2000

    bmw = Distance(BMW(diesel))
    calc_distance(bmw, DISTANCE)

    audi = Distance(Audi(benzine))
    calc_distance(audi, DISTANCE)

    mercedes = Distance(Mercedes(diesel))
    calc_distance(mercedes, DISTANCE)


if __name__ == "__main__":
    main()
