from abc import ABC, abstractmethod
import json
import yaml
import xml.etree.ElementTree as ET

from typing import List

from factorys import CarMTCarFactory, CarATCarFactory, AbcCarFactory

OUTSIDE_DB = {}


def print_db():
    for k, v in OUTSIDE_DB.items():
        print('\U0001F90C ', k, v)


class InterfaceLoader(ABC):
    @abstractmethod
    def load(self):
        pass


class Loader(InterfaceLoader):

    def __init__(self, pwd_file, spliter: str = None):
        self.pwd_file = pwd_file
        self.db = {}

        self.spliter = spliter if spliter is not None else ';'
        self.factory = {
            "mt": CarMTCarFactory(),
            "at": CarATCarFactory(),
        }

    @abstractmethod
    def load(self):
        pass

    def construct_car(self, t_type, engine_rpm, engine_idle, t_ratio_list, t_name, car_name):
        factory = self.factory.get(t_type)

        engine = factory.create_engine(engine_rpm, engine_idle)
        transmission = factory.create_transmission(t_ratio_list, t_name)

        return factory.create_car(engine, transmission, car_name)


class ProxyLoader(InterfaceLoader):

    def __init__(self, daddies: List[Loader]):
        self.daddies = daddies
        self.catalog = {}

    def load(self):
        for daddy in self.daddies:
            self.catalog.update(daddy.load())

        self.save() # ?

    def load2(self):
        for daddy in self.daddies:
            self.catalog.update(daddy.load())

        return self.catalog # ?

    # === ??? ====
    def save(self):
        OUTSIDE_DB.update(self.catalog)
    # === ??? ====


class ProxyLoader2(InterfaceLoader):

    def __init__(self, file_list: list):
        self.file_dict: dict = self.get_type_file_dict(file_list)
        self.daddies = {
            'csv': LoadFromCSV,
            'json': LoadFromJSON,
            'xml': LoadFromXML,
            'yaml': LoadFromYAML
        }
        self.catalog = {}

    def load(self):
        for type_file, file_path in self.file_dict.items():
            loader = self.daddies.get(type_file)
            self.catalog.update(loader(file_path).load())

        self.save() # ?
        return self.catalog # ?

    # === ??? ====
    def save(self):
        OUTSIDE_DB.update(self.catalog)
    # === ??? ====

    def get_type_file_dict(self, file_list):
        file_dict = {}

        for file_path in file_list:
            type_file = file_path.split('.')[1]
            file_dict.update({
                type_file: file_path
            })

        return file_dict


class LoadFromCSV(Loader):

    def load(self):
        with open(self.pwd_file, 'r') as f:
            for i in f:
                data = i.split(self.spliter)

                code = data[0]
                car_name = data[1]
                engine_rpm = int(data[2])
                engine_idle = int(data[3])
                t_ratio_list = [float(i) for i in data[4].split(',')]
                t_name = data[5]
                t_type = data[6]

                car = self.construct_car(t_type, engine_rpm, engine_idle, t_ratio_list, t_name, car_name)

                self.db.update({code: car})

        # self.db.update(self.db)
        return self.db


class LoadFromJSON(Loader):

    def load(self):
        with open(self.pwd_file) as file:
            j = json.load(file)
            for e in j:
                code = e.get('code')
                car_name = e.get("car_model")
                engine_rpm = e.get("engine_max_rpm")
                engine_idle = e.get("engine_idle")
                t_ratio_list = e.get("transmission_ratio_list")
                t_name = e.get("transmission_model")
                t_type = e.get("transmission_type")

                car = self.construct_car(t_type, engine_rpm, engine_idle, t_ratio_list, t_name, car_name)

                self.db.update({code: car})

        # self.db.update(self.db)
        return self.db


class LoadFromXML(Loader):
    def load(self):

        root = ET.parse(self.pwd_file).getroot()

        for i in root.findall('element'):
            code = i.find('code').text
            car_name = i.find("car_model").text
            engine_rpm = int(i.find("engine_max_rpm").text)
            engine_idle = int(i.find("engine_idle").text)
            t_ratio_list = [e.text for e in i.findall("./transmission_ratio_list/element")]
            t_name = i.find("transmission_model").text
            t_type = i.find("transmission_type").text

            car = self.construct_car(t_type, engine_rpm, engine_idle, t_ratio_list, t_name, car_name)

            self.db.update({code: car})

        # self.db.update(self.db)
        return self.db


class LoadFromYAML(Loader):

    def load(self):
        with open(self.pwd_file, 'r') as f:
            file = yaml.safe_load(f)
            for i in file:
                code = i.get('code')
                car_name = i.get("car_model")
                engine_rpm = i.get("engine_max_rpm")
                engine_idle = i.get("engine_idle")
                t_ratio_list = i.get("transmission_ratio_list")
                t_name = i.get("transmission_model")
                t_type = i.get("transmission_type")

                car = self.construct_car(t_type, engine_rpm, engine_idle, t_ratio_list, t_name, car_name)

                self.db.update({code: car})

            # self.db.update(self.db)
            return self.db


def client(loader: InterfaceLoader):
    data = loader.load()
    OUTSIDE_DB.update(data)


if __name__ == "__main__":

    _csv = LoadFromCSV('load_cars.csv', spliter=";")
    _json = LoadFromJSON('load_cars.json')
    _xml = LoadFromXML('load_cars.xml')
    _yaml = LoadFromYAML('load_cars.yaml')

    proxy = ProxyLoader([_csv, _json, _xml, _yaml])
    proxy.load()

    data = proxy.load2()
    OUTSIDE_DB.update(data)

    # V-2
    # files_list = ['load_cars.csv', 'load_cars.json', 'load_cars.xml', 'load_cars.yaml']
    # proxy = ProxyLoader2(files_list)
    # proxy.load()

    print_db()