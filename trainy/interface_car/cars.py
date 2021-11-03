from abc import ABC, abstractmethod
from engines import Engine
from transmissions import GearBox, AT, MT
from tqdm import tqdm



class Car(ABC):
    def __init__(self, engine: Engine, transmission: GearBox):
        self.engine = engine
        self.transmission = transmission

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def speed_up(self):
        pass

    @abstractmethod
    def speed_down(self):
        pass


class CarMT(Car):
    transmission: MT

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.status = 'Go'

    def start(self):
        self.engine.start()
        self.status = 'Engine is Started'

    def stop(self):
        self.engine.stop()
        self.status = 'Engine is Stoped'

    def speed_up(self):
        new_rpm = self.engine.get_current_rpm() + 100

        if self.engine.get_current_rpm() == 0:
            self.status = '\033[91mFirst Start Engine <S>\033[0m'
        elif new_rpm > self.engine.max_rpm:
            self.engine.set_rpm(new_rpm - 500)
            self.status = '\033[91mRATATATATATATATATAT\033[0m'
        else:
            self.engine.set_rpm(new_rpm)
            self.status = 'RPM_UP'

    def speed_down(self):
        new_rpm = self.engine.get_current_rpm() - 100
        if new_rpm < 0:
            self.status = '\033[91mEngine is down. See you at retake\033[0m'
            self.engine.set_rpm(0)
        else:
            self.engine.set_rpm(new_rpm)
            self.status = 'RPM_Down'

    def shift_gear(self, gear):
        self.transmission.set_gear(gear)

    def gear_length(self):
        return self.transmission.gear_length()


class CarAT(Car):
    transmission: AT

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def speed_up(self):
        new_rpm = self.engine.get_current_rpm() + 100
        self.engine.set_rpm(new_rpm)

    def speed_down(self):
        new_rpm = self.engine.get_current_rpm() - 100
        self.engine.set_rpm(new_rpm)
