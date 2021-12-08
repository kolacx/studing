from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET

from factorys import CarMTCarFactory, CarATCarFactory, AbcCarFactory


class Loader(ABC):
    DB = {}

    def __init__(self, pwd_file, spliter: str = None):
        self.pwd_file = pwd_file

        self.spliter = spliter if spliter is not None else ';'
        self.factory = {
            "mt": CarMTCarFactory(),
            "at": CarATCarFactory(),
        }

    @classmethod
    def _save_db(cls, data):
        cls.DB.update(data)

    @abstractmethod
    def load(self):
        pass

    @classmethod
    def print_db(cls):
        for k, v in cls.DB.items():
            print(k, '\U0001F90C ', v)

    def _construct_car(self, t_type, engine_rpm, engine_idle, t_ratio_list, t_name, car_name):
        factory = self.factory.get(t_type)

        engine = factory.create_engine(engine_rpm, engine_idle)
        transmission = factory.create_transmission(t_ratio_list, t_name)

        return factory.create_car(engine, transmission, car_name)


class LoadFromCSV(Loader):
    def load(self):
        temp = {}

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

                car = self._construct_car(t_type, engine_rpm, engine_idle, t_ratio_list, t_name, car_name)

                temp.update({code: car})

        self._save_db(temp)


class LoadFromJSON(Loader):
    def load(self):
        temp = {}
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

                car = self._construct_car(t_type, engine_rpm, engine_idle, t_ratio_list, t_name, car_name)

                temp.update({code: car})

        self._save_db(temp)


class LoadFromXML(Loader):
    def load(self):
        temp = {}
        root = ET.parse(self.pwd_file).getroot()

        for i in root.findall('element'):
            code = i.find('code').text
            car_name = i.find("car_model").text
            engine_rpm = int(i.find("engine_max_rpm").text)
            engine_idle = int(i.find("engine_idle").text)
            t_ratio_list = [e.text for e in i.findall("./transmission_ratio_list/element")]
            t_name = i.find("transmission_model").text
            t_type = i.find("transmission_type").text

            car = self._construct_car(t_type, engine_rpm, engine_idle, t_ratio_list, t_name, car_name)

            temp.update({code: car})

        self._save_db(temp)


if __name__ == "__main__":

    _csv = LoadFromCSV('load_cars.csv', spliter=";")
    _json = LoadFromJSON('load_cars.json')
    _xml = LoadFromXML('load_cars.xml')

    _csv.load()
    _json.load()
    _xml.load()

    Loader.print_db()
