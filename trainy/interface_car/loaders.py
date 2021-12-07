from abc import ABC, abstractmethod

from factorys import CarMTFactory, TransmissionMTFactory, Manual, Authomatic
from builders import EngineBuilder


class Loader(ABC):
    def __init__(self, pwd_file):
        self.pwd_file = pwd_file
        self.db = {}

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def _save_db(self, data):
        pass

    def build_car(self, f: [Manual, Authomatic], engine_rpm, transmission_ratio_list, transmission_name, car_name):
        engine = EngineBuilder().set_max_rpm(engine_rpm).build()
        transmission = f.create_transmission(transmission_ratio_list, transmission_name)
        car = f.create_car(engine, transmission, car_name)

        return car


class LoadFromCSV(Loader):
    def __init__(self, pwd_file, spliter: str):
        super().__init__(pwd_file)
        self.spliter = spliter

    def print_db(self):
        for k, v in self.db.items():
            print(k, '\U0001F90C ', v)

    def _save_db(self, data):
        self.db.update(data)

    def load(self):
        temp = {}

        with open(self.pwd_file, 'r') as f:
            for i in f:
                data = i.split(self.spliter)

                car_name = data[0]
                engine_rpm = int(data[1])
                transmission_ratio_list = [data[2]]
                transmission_name = data[3]
                transmission_type = data[4]

                type = Manual() if transmission_type == 'mt' else Authomatic()

                car = self.build_car(type, engine_rpm, transmission_ratio_list, transmission_name, car_name)

                code = f"{car_name}_{engine_rpm}_{transmission_name}"

                temp.update({code: car})

        self._save_db(temp)


# if __name__ == "__main__":
#     print('Common')
#
#     cars = LoadFromCSV('cars.csv', ';')
#     cars.load()
#     cars.print_db()
