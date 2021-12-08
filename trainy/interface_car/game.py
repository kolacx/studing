'''
Пусть каждая фабрика


Очертить сначало задачи которые я хочу решить. Относительно машины.
Создание машины с нуля.
Получить придефолт.


Машину нужно создавать как.


Описать участников которые будут пользоваться моим приложением.
Клиенты.
Фабрики.

Клиенту дать доступ только к тому что выпустил завод.

Фабрике выдать досутп на создание машины.
'''
from display import DisplayMT, DisplayAT
from factorys import CarATCarFactory, CarMTCarFactory
from loaders import LoadFromCSV
from simulator import SimulatorMT, SimulatorAT
from transmissions import MT


class LO(LoadFromCSV):
    def get_car_by_code(self, code):
        return self.db.get(code)


if __name__ == "__main__":
    print('Game')

    loader = LO('load_cars.csv', ';')
    loader.load()

    car = loader.get_car_by_code('bmw1_1111_zf1_mt')
    display = DisplayMT(car)
    simulator = SimulatorMT(car, display)

    simulator.drive()


