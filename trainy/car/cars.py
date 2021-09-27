from abc import ABC, abstractmethod
from engine import Engine
from trainy.car.transmission import Transmission, Manual, Automatic, CarInterfaceTransmission
from wheels import Wheel


class Car(ABC):
    """
    Класс Car является Поставщиком если смотреть со стороны одного из Main(клиента)
    Для класса Car поставщиком является класс Engine.
    """

    def __init__(self, brand, engine: Engine, wheel: Wheel, transmission: CarInterfaceTransmission, formula=None):
        self.brand = brand
        self.formula = formula

        self.engine = engine
        self.transmission = transmission
        self.wheel = wheel

        if formula is None:
            self.formula = self._default_avg_speed_calc

    # def transmission_ctrl(self, transmission):
    #     if isinstance(transmission, Manual):
    #         return transmission
    #     elif isinstance(transmission, Automatic):
    #         return transmission

    def get_average_speed(self):
        return self.formula(self)

    def _default_avg_speed_calc(self, car):
        average_speed = car.engine.engine_load() * car.engine.engine_volume
        return average_speed

    def current_speed(self, rpm):
        if self.transmission.get_current_gear() == 0:
            return 0

        r_cm = (self.wheel.radius * 2.54) * 10
        profile_height = self.wheel.tire.width * (self.wheel.tire.height / 100)
        w_h = (profile_height * 2 + r_cm) / 10

        speed = rpm * (w_h / ((self.transmission.get_main_steam() * self.transmission.get_ratio()) * 530.616))

        return speed
