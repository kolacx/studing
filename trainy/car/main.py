from cars import Car, Performance
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
     
8) 
    Расчитать avarage_speed.
    Только у дизельного Мерседеса производительность на 10 процентов больше
    
9) 
    Оказывается у нас можность двигателя меняется не только у Мерседеса, а и у других машин также.
    
10)
    Если двигатель бензиновый то к performance + 2. А если двигатель Дизельный -2
    
11) 
    Найти способ Вынести формулу прощета get_average_speed за рамки моего решения.
'''


class BMW(Car):
    def __init__(self, engine, performance, formula):
        super().__init__('BMW', engine, 1000, performance=performance, formula=formula)


class Audi(Car):
    def __init__(self, engine, performance, formula):
        super().__init__('Audi', engine, 1500, performance=performance, formula=formula)


class Mercedes(Car):
    def __init__(self, engine):
        super().__init__('Mercedes', engine, 2000)


def calc_time(car: Car, distance: int):
    """
        Является Решением для Килента (Main)
    """
    time = (distance / car.get_average_speed()) * 60
    print(f'Машина {car.brand} проедит {distance}Km, за {round(time, 2)} минут @ {car.engine}')


def calc_time2(car: Car, distance: int):
    """
        Является Решением для Килента (Main)
    """
    time = (distance / car.get_average_speed()) * 60
    time -= 6
    print(f'Машина {car.brand} проедит {distance}Km, за {round(time, 2)} минут @ {car.engine}')


def formula_diesel(s):
    ret = s.engine.engine_load() * s.engine.engine_volume
    return ret - 2


def formula_benzine(s):
    ret = s.engine.engine_load() * s.engine.engine_volume
    return ret + 2


def main():
    """
        Является решением для Бизнеса.
        Его поставщики это Engine и Car
    """
    diesel_bmw = Diesel(2, 100, type='Diesel')
    diesel_mercedes = Diesel(2, 100, type='Diesel')
    benzine_audi = Benzine(4, 200, type='Benzine')

    DISTANCE = 1000

    bmw = Car('BMW', diesel_bmw, 1000, performance=1.1, formula=formula_diesel)
    calc_time(bmw, DISTANCE)

    audi = Car('Audi', benzine_audi, 1500, formula=formula_benzine)
    calc_time(audi, DISTANCE)

    mercedes = Car('Mercedes', diesel_mercedes, 2000, formula=formula_diesel)
    calc_time2(mercedes, DISTANCE)


if __name__ == "__main__":
    main()
