from abc import ABC, abstractmethod


class InterfaceTransmission(ABC):

    @abstractmethod
    def up_gear(self):
        pass

    @abstractmethod
    def down_gear(self):
        pass


class InterfaceCVT(ABC):

    @abstractmethod
    def rotate(self):
        pass


class Transmission(ABC):
    def __init__(self, gearbox_len: int):
        self.gearbox_len = gearbox_len


class Manual(Transmission):
    def __init__(self, gearbox_len):
        super().__init__(gearbox_len)


class Automatic(Transmission):
    def __init__(self, gearbox_len):
        super().__init__(gearbox_len)


class ContinuouslyVariable(Transmission):
    def __init__(self, gearbox_len):
        super().__init__(gearbox_len)