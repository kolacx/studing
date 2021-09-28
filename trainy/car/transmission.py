from abc import ABC, abstractmethod
import numpy as np

'''
Каробка.
Абстракция коробки.
    Что такое коробка. Коробка механихм передающий мощность от двигателя к редуктору.
    
    Получается зависимость от двигателя, это обороты которые выдает двигатель.
    
    Обороты начинают крутить коробку
    Выход коробки, передача оборотов на Редуктор.
    
    Получается единственное что делает коробка это изменяет обороты которые в дальнейшем передадутся редуктору в N раз.
    
Свойства коробки. 
    Множитель.
    
    Передача дальше.

====================================================

Детализация коробки
    Средне статистическая коробка имеет-
        Передачи. - которые являются делителями (Список делителей)

'''


class Transmission(ABC):
    def __init__(self, ratio_list):
        self.ratio = 0
        self.ratio_list = ratio_list

    def exit(self, rpm):
        return self.ratio / rpm


class MT(Transmission):
    def set_manual_gear(self, gear):
        self.ratio = self.ratio_list[gear - 1]


class AT(Transmission):
    def up(self):
        gear = self.ratio_list.index(self.ratio) + 1
        self.ratio = self.ratio_list[gear]

    def down(self):
        gear = self.ratio_list.index(self.ratio) - 1
        self.ratio = self.ratio_list[gear]


class CVT(AT):
    def __init__(self, down_ratio, up_ratio):
        self.ratio_list = np.arange(down_ratio, up_ratio, 0.1)
        super().__init__(ratio_list=self.ratio_list)























# class CarInterfaceTransmission(ABC):
#
#     @abstractmethod
#     def get_brand(self):
#         pass
#
#     @abstractmethod
#     def get_gear_ratios(self):
#         pass
#
#     @abstractmethod
#     def get_main_steam(self):
#         pass
#
#     @abstractmethod
#     def get_current_gear(self):
#         pass
#
#     @abstractmethod
#     def get_ratio(self):
#         pass
#
#
# class HumanInterfaceTransmission(ABC):
#
#     @abstractmethod
#     def up_gear(self):
#         pass
#
#     @abstractmethod
#     def down_gear(self):
#         pass
#
#     @abstractmethod
#     def get_ratio(self):
#         pass
#
#
# class TransmissionInterface(CarInterfaceTransmission, HumanInterfaceTransmission):
#     def __init__(self, brand: str, gear_ratios: list, main_steam: float):
#         self.brand = brand
#         self.gear_ratios = gear_ratios
#         self.main_steam = main_steam
#
#     @abstractmethod
#     def get_brand(self):
#         pass
#
#     @abstractmethod
#     def get_gear_ratios(self):
#         pass
#
#     @abstractmethod
#     def get_main_steam(self):
#         pass
#
#     @abstractmethod
#     def get_current_gear(self):
#         pass
#
#     @abstractmethod
#     def get_ratio(self):
#         pass
#
#     @abstractmethod
#     def up_gear(self):
#         pass
#
#     @abstractmethod
#     def down_gear(self):
#         pass
#
#
# class Manual(TransmissionInterface):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.current_gear = 0
#
#     def _set_gear(self, gear):
#         if gear > len(self.gear_ratios) or gear < 0:
#             raise ValueError(f'gear: {gear}. out of Gear Box range: 0 - {len(self.gear_ratios)}')
#
#         self.current_gear = gear
#
#     def up_gear(self):
#         self._set_gear(self.current_gear + 1)
#
#     def down_gear(self):
#         self._set_gear(self.current_gear - 1)
#
#     def get_ratio(self):
#         return self.gear_ratios[self.current_gear - 1]
#
#     def get_brand(self):
#         return self.brand
#
#     def get_gear_ratios(self):
#         return self.gear_ratios
#
#     def get_main_steam(self):
#         return self.main_steam
#
#     def get_current_gear(self):
#         return self.current_gear
#
#
# class Automatic(Manual):
#     def __init__(self, *args):
#         super().__init__(*args)
