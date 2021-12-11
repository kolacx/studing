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


'''


class PredeterminedCarFactory(ABC):
    @abstractmethod
    def create_car(self, key) -> Car:
        pass


class CodePredeterminedCarFactory(PredeterminedCarFactory):
    def create_car(self, key: str) -> Car:
        return OUTSIDE_DB.get(key)


class ListPredeterminedCarFactory(PredeterminedCarFactory):
    def create_car(self, keys: List[str]) -> List[Car]:
        cars = []
        for k in keys:
            cars.append(OUTSIDE_DB.get(k))

        return cars

