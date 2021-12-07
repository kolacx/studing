
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
from cars import Car, CarMT, CarAT
from loaders import LoadFromCSV
from display import DisplayMT
from factorys import Manual, Authomatic
from simulator import Simulator
from transmissions import MT


def build_simulator(car: [CarMT, CarAT]) -> Simulator:
    fabric = Manual() if isinstance(car.transmission, MT) else Authomatic()

    display = fabric.create_display(car)
    simulator = fabric.create_simulator(car, display)
    return simulator


class LO(LoadFromCSV):
    def get_car_by_code(self, code):
        return self.db.get(code)


if __name__ == "__main__":
    print('Game')

    loader = LO('cars.csv', ';')
    loader.load()

    car = loader.get_car_by_code('bmw1_1111_zf1')

    simulator = build_simulator(car)
    simulator.drive()
