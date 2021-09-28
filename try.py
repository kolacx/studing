from abc import ABC, abstractmethod
import numpy as np


class Transmission:
    def __init__(self, ratio_list):
        self.ratio = 0
        self.ratio_list = ratio_list

    def exit(self, rpm):
        return self.ratio / rpm


class MT(Transmission):
    def set_gear(self, gear):
        self.ratio = self.ratio_list[gear - 1]


class AT(MT):
    pass


class CVT(AT):
    def __init__(self, down_ratio, up_ratio):
        self.ratio_list = np.arange(down_ratio, up_ratio, 0.1)
        super().__init__(ratio_list=self.ratio_list)


class Controller(ABC):
    def __init__(self, transmission, controller):
        self.transmission = transmission
        self.control = controller


class MTController(Controller):
    def __init__(self, transmission: MT):
        super().__init__(transmission, controller=self)

    def neutral(self):
        pass

    def shift(self, gear):
        self.transmission.set_gear(gear)


class ATController(Controller):
    def __init__(self, transmission: AT):
        super().__init__(transmission, controller=self)

    def parking(self):
        self.transmission.ratio = 0

    def revers(self):
        self.transmission.ratio = -self.transmission.ratio

    def neutral(self):
        self.transmission.ratio = 0

    def drive(self):
        self.transmission.ratio = self.transmission.ratio_list[0]

    def up(self):
        gear = self.transmission.ratio_list.index(self.transmission.ratio) + 1
        self.transmission.set_gear(gear)

    def down(self):
        gear = self.transmission.ratio_list.index(self.transmission.ratio) - 1
        self.transmission.set_gear(gear)


class Car:
    def __init__(self, tr_ctrl: Controller):
        self.tr_ctrl = tr_ctrl


if __name__ == "__main__":
    mt = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83])
    mt_controller = MTController(mt)
    at = AT([4.23, 2.53, 1.67, 1.23, 1, 0.83])
    at_ctrl = ATController(at)
    cvt = CVT(3, 6)

    car = Car(mt_controller)

    car.tr_ctrl.control.shift(3)

    car2 = Car(at_ctrl)
    car2.tr_ctrl.control.drive()
    print(car2.tr_ctrl.transmission.exit(1500))
