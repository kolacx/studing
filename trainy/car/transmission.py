from abc import ABC, abstractmethod


class CarInterfaceTransmission(ABC):

    @abstractmethod
    def get_brand(self):
        pass

    @abstractmethod
    def get_gear_ratios(self):
        pass

    @abstractmethod
    def get_main_steam(self):
        pass

    @abstractmethod
    def get_current_gear(self):
        pass

    @abstractmethod
    def get_ratio(self):
        pass


class HumanInterfaceTransmission(ABC):

    @abstractmethod
    def up_gear(self):
        pass

    @abstractmethod
    def down_gear(self):
        pass

    @abstractmethod
    def get_ratio(self):
        pass


class TransmissionInterface(CarInterfaceTransmission, HumanInterfaceTransmission):
    def __init__(self, brand: str, gear_ratios: list, main_steam: float):
        self.brand = brand
        self.gear_ratios = gear_ratios
        self.main_steam = main_steam

    @abstractmethod
    def get_brand(self):
        pass

    @abstractmethod
    def get_gear_ratios(self):
        pass

    @abstractmethod
    def get_main_steam(self):
        pass

    @abstractmethod
    def get_current_gear(self):
        pass

    @abstractmethod
    def get_ratio(self):
        pass

    @abstractmethod
    def up_gear(self):
        pass

    @abstractmethod
    def down_gear(self):
        pass


class Manual(TransmissionInterface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_gear = 0

    def _set_gear(self, gear):
        if gear > len(self.gear_ratios) or gear < 0:
            raise ValueError(f'gear: {gear}. out of Gear Box range: 0 - {len(self.gear_ratios)}')

        self.current_gear = gear

    def up_gear(self):
        self._set_gear(self.current_gear + 1)

    def down_gear(self):
        self._set_gear(self.current_gear - 1)

    def get_ratio(self):
        return self.gear_ratios[self.current_gear - 1]

    def get_brand(self):
        return self.brand

    def get_gear_ratios(self):
        return self.gear_ratios

    def get_main_steam(self):
        return self.main_steam

    def get_current_gear(self):
        return self.current_gear


class Automatic(Manual):
    def __init__(self, *args):
        super().__init__(*args)
