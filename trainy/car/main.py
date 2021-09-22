from abc import ABC, abstractmethod
from cars import Car
from engine import Diesel, Benzine

'''
    Поставщик
    Решение
    Клиент

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
    "Машина BMW проедит 2000m, за 1000.0 минут @ Бензин"е трогать мейн
    
    
7)
    Не трогать менй +
    Тип двигателя перенести в Engine +
    Избавится от класов Distance +
    Избавится от torque +
    repr перенести в верхний класс +
     

'''


class BMW(Car):
    def __init__(self, engine):
        super().__init__('BMW', engine, 1000)


class Audi(Car):
    def __init__(self, engine):
        super().__init__('Audi', engine, 1500)


class Mercedes(Car):
    def __init__(self, engine):
        super().__init__('Mercedes', engine, 2000)


def calc_distance(car: Car, distance: int):
    """
        Является Решением для Килента (Main)
    """
    time = (distance / car.get_average_speed()) * 60
    print(f'Машина {car.brand} проедит {distance}Km, за {round(time, 2)} минут @ {car.engine}')


def calc_distance2(car: Car, distance: int):
    """
        Является Решением для Килента (Main)
    """
    time = (distance / car.get_average_speed()) * 60
    time -= 6
    print(f'Машина {car.brand} проедит {distance}Km, за {round(time, 2)} минут @ {car.engine}')


def main():
    """
        По факту является Клиентом для нашего прложения.
        Его поставщики это Engine и Car
    """
    diesel_bmw = Diesel(2, 100, type='Diesel')
    diesel_mercedes = Diesel(3, 150, type='Diesel')
    benzine_audi = Benzine(4, 200, type='Benzine')

    DISTANCE = 1000

    bmw = BMW(diesel_bmw)
    calc_distance(bmw, DISTANCE)

    audi = Audi(benzine_audi)
    calc_distance(audi, DISTANCE)

    mercedes = Mercedes(diesel_mercedes)
    calc_distance2(mercedes, DISTANCE)


if __name__ == "__main__":
    main()
