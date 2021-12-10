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


class Loader(ABC):

    def __init__(self):
        self.db = {}
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


class FileLoader(Loader):

    def __init__(self, pwd_file):
        super().__init__()
        self.pwd_file = pwd_file

    def load(self):
        NotImplementedError('Need Implements')


class LoadFromCSV(FileLoader):

    def __init__(self, pwd_file, spliter):
        super().__init__(pwd_file)
        self.spliter = spliter if spliter is not None else ';'

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

        return self.db


class LoadFromJSON(FileLoader):

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

        return self.db


class LoadFromXML(FileLoader):

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

        return self.db


class LoadFromYAML(FileLoader):

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

        return self.db


class ListLoader(Loader):

    def __init__(self, daddies: List[Loader]):
        super().__init__()
        self.daddies = daddies

    def load(self):
        for daddy in self.daddies:
            self.db.update(daddy.load())

        return self.db


if __name__ == "__main__":

    loader = ListLoader([
        LoadFromCSV('load_cars.csv', spliter=";"),
        LoadFromJSON('load_cars.json'),
        LoadFromXML('load_cars.xml'),
        LoadFromYAML('load_cars.yaml')
    ])
    data = loader.load()

    OUTSIDE_DB.update(data)
    print_db()
