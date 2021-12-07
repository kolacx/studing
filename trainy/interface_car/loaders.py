from abc import ABC, abstractmethod

from factorys import BmwMTFactory, BmwATFactory, AbcFactory


class Loader(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def _save_db(self, data):
        pass

    # def build_car(self, f: AbcFactory, engine_rpm, t_ratio_list, t_name, car_name):
    #     engine = f.create_engine(engine_rpm)
    #     transmission = f.create_transmission(t_ratio_list, t_name)
    #     car = f.create_car(engine, transmission, car_name)
    #
    #     return car


class LoadFromCSV(Loader):
    def __init__(self, pwd_file, spliter: str):
        self.pwd_file = pwd_file
        self.db = {}
        self.spliter = spliter

    def print_db(self):
        for k, v in self.db.items():
            print(k, '\U0001F90C ', type(v.transmission))

    def _save_db(self, data):
        self.db.update(data)

    def load(self):
        temp = {}

        with open(self.pwd_file, 'r') as f:
            for i in f:
                data = i.split(self.spliter)

                car_name = data[0]
                engine_rpm = int(data[1])
                t_ratio_list = [float(i) for i in data[2].split(',')]
                t_name = data[3]
                t_type = data[4]

                factory = BmwMTFactory() if t_type == 'mt' else BmwATFactory()

                engine = factory.create_engine(engine_rpm)
                transmission = factory.create_transmission(t_ratio_list, t_name)
                car = factory.create_car(engine, transmission, car_name)

                # car = self.build_car(factory, engine_rpm, t_ratio_list, t_name, car_name)

                code = f"{car_name}_{engine_rpm}_{t_name}"

                temp.update({code: car})

        self._save_db(temp)


# if __name__ == "__main__":
#     print('Common')
#
#     cars = LoadFromCSV('cars.csv', ';')
#     cars.load()
#     cars.print_db()
