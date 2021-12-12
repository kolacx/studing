from abc import ABC, abstractmethod
from typing import List

from cars import Car, CarMT, CarAT
from engines import Engine
from settings import OUTSIDE_DB
from transmissions import GearBox, AT, MT


class AbcCarFactory(ABC):
    def create_engine(self, max_rpm: int, idle: int) -> Engine:
        return Engine(max_rpm, idle)

    @abstractmethod
    def create_transmission(self, ratio_list: list, name: str) -> GearBox:
        pass

    @abstractmethod
    def create_car(self, engine: Engine, transmission: GearBox, name: str) -> Car:
        pass


class CarATCarFactory(AbcCarFactory):
    def create_transmission(self, ratio_list: list, name: str) -> AT:
        return AT(ratio_list, name)

    def create_car(self, engine: Engine, transmission: AT, name: str) -> CarAT:
        return CarAT(engine, transmission, name)


class CarMTCarFactory(AbcCarFactory):
    def create_transmission(self, ratio_list: list, name: str) -> MT:
        return MT(ratio_list, name)

    def create_car(self, engine: Engine, transmission: MT, name: str) -> CarMT:
        return CarMT(engine, transmission, name)


'''
Давай распишем что мы понимаем, если мы чтото понимаем....
Пообщаемся сами с собой.

Задача звучит так " Фабрика для создание предзаданных машин ".

ФАКТ: Предзаданные машины храняться у нас в БД, так как они уже загружены.
Тобишь нам нужен функционал который будет возвращать нам машину, которая уже существует у нас в нутри приложения.

Чтобы вернуть нам машину, нам нужно понять какую от нас машину требуют. Для такой ситуаци и мы предусмотрели поле CODE,
по которому мы можем идентифицировать машину. Код выглядит так - "ks_6500_X4BA4_at"
Больше ничего не нужно (Мы ето можем утверждать потому что, мы знаем как устроенна наша БД в которой храняться машины.)

Получается наша задача предусмотреть только эту возможность.
У нас будет Класс с методом возвращаюший машину. Ему пофиг какая машина вернется (АТ или МТ). У него задача одна
вернуть машину приняв при этом CODE машины.

Вход: CODE машины.
Выход: Результатом выполнения нашего кода ето конкретная машина.

Почему ето должна быть фабрика!?
Та х*й его знает!

Фабрику мы применяем тогда, когда зарание не знаем с каким типом данных мы будем работать со стороны клиента.
Тобишь клиент решает с чем он хочет работать.
Причем что фабрика всегда создает.
Можно ли считать что возврат требуемого с БД является "созданием"???

Тут нам такая возможность не нужна. Так как мы ищем только по Коду.

НО! Зная Санька он щяс доебется до меня тем что:
- А прикинь нам нашу машину нужно будет искать не по коду а по Коробке! Автомат или не автомат!

Ну тогда мы понимаем что нам нужна фабрика, 
так как мы не знаем изначально по каким параметрам нам нужно искать автомобиль

Получается у нас появляется фабрика, у которой есть метод возврата машины. Все.

Далее мы описываем классы с конкретным поиском.

--
Давай дальше поищем возможные варианты развития событий.

Что у нас получается сейчас....
У нас есть фабрика по поиску автомобиля/автомобилей.
Мы можем задать себе критерий поиска.

..................................... хз...

Еще раз суть. 
Нужно реализовать получение машины по коду.

class SearchCarByCode:

    def create_car(self, code) -> Car:
        return OUTSIDE_DB.get(code)

Шикарное решение, но мы допускаем что могут быть разные критерии поиска.
Чтобы в данной реализации изменить то по чему мы ещем, нужно унаследовать класс, и переписать метод так как нам надо.

class SearchByModel(SearchByCode):
    def create_car(self, model) -> Car:
        for i in OUTSIDE_DB.value():
            if i.model == model:
                return i


Чета шляпа кажись получаетсья.

Версия 2

class Search(ABC):
    
    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def create(self) -> Car:
        pass
    

class ByCode(Search):
    
    def create(self) -> Car:
        return OUTSIDE_DB.get(self.parameter)
        
Решил переименовать класс, ато приелось называние.

По данному коду получается нам пофиг какой нам параметр зададут, мы сможем по любому их них найти нашу машину.
Создав новый класс, унаследовав его от Абстракции, и реализовав бастрактный метод.                

Что делать если у нас появиться 2 параметра для поиска?
Что делать если у нас появиться 3 параметра для поиска?

Какаято все хуйня

Может быть нужно зайти со всем с другой стороны.....
ВОпросто тогда с каокй.
Идей 0

Вроде бы мы договорились о том что у нас "поиск" будет работать только по коду.
Но опятьже как я понимаю, мы должны думать более маштабней и понять какой частью большой системы будет "поиск по коду".

У нас есть 1 винтик. Ето то от чего мы можем одтолкнутся

------------------------||||

Подумаем о том чтобы сделать класс у которого будет набор функций по работе с каталогом.
У нас есть общий класс CatalogCars:
первый же метод будет get_car_by_code(code)
Который будет возвращать нам мошину.

Если появятся новые требования к получению машины, мы это реализовывать будем добавлением нового метода.

----||||

Давай подумаем по поводу универсального каталога.
Первое что пришло в голову, ето то что мы можем работать с разными каталогами.
Например Машины, Двигателя, Трансмиссии.

Тогда получается у нас будет общий класс каталог и производные/

'''


class Catalog(ABC):
    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def by_code(self, code):
        pass


class CarCatalog(Catalog):

    def _get_by_arg(self, ar):
        cars = []
        for car in OUTSIDE_DB.values():
            if car.engine.get_max_rpm() == ar:
                cars.append(car)

        return cars

    def all(self):
        return OUTSIDE_DB

    def by_code(self, code):
        return OUTSIDE_DB.get(code)

    def by_engine_maxrpm(self, rpm) -> List[Car]:
        return self._get_by_arg(rpm)

    def by_transmission_type(self, t_type) -> List[Car]:
        return self._get_by_arg(t_type)
