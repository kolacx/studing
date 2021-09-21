from abc import ABC, abstractmethod
from cars import Car, Distance, DistanceMercedes
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
    Когда мы устанавливаем Дизельные двигателя в разные автомобили, коефициент мощностми меняется. +
    
5) 
    Все машины должны проезжать одно и тоже растояние. +
    подогнать цифры так чтобы бмв проезжало за 10 минут. +
    
6) 
    Только у Mercedes время проезда занимает -6 минут от основного.
    "Машина BMW проедит 2000m, за 1000.0 минут @ Бензин"

'''


class BMW(Car):
    def __init__(self, engine):
        super().__init__('BMW', engine, 1000)


class Audi(Car):
    def __init__(self, engine):
        super().__init__('Audi', engine, 1500)


class Mercedes(Car):
    def __init__(self, engine):
        super().__init__('Mercedes', engine, 1000)


def calc_distance(dis: Distance, distance: int):
    print(f'Машина {dis.car.brand} проедит {distance}m, за {round(dis.distance(distance), 2)} '
          f'минут @ {dis.car.engine}')


def main():

    diesel_bmw = Diesel(2, 185.12, 1)
    diesel_mercedes = Diesel(3, 185.12, 2)
    benzine_audi = Benzine(4, 250.65)

    DISTANCE = 2000

    bmw = Distance(BMW(diesel_bmw))
    calc_distance(bmw, DISTANCE)

    audi = Distance(Audi(benzine_audi))
    calc_distance(audi, DISTANCE)

    mercedes = DistanceMercedes(Mercedes(diesel_mercedes))
    calc_distance(mercedes, DISTANCE)


if __name__ == "__main__":
    main()
