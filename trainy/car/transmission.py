from abc import ABC, abstractmethod


class Transmission(ABC):
    def __init__(self, brand: str, gear_ratios: list, main_steam: float):
        self.brand = brand
        self.gear_ratios = gear_ratios
        self.main_steam = main_steam


class Manual(Transmission):
    def __init__(self, *args, current_gear=0):
        super().__init__(*args)
        self.current_gear = current_gear

    def _set_gear(self, gear):
        if gear > len(self.gear_ratios) or gear < 0:
            raise ValueError(f'gear: {gear}. out of Gear Box range: 0 - {len(self.gear_ratios)}')

        self.current_gear = gear

    def up_gear(self):
        self._set_gear(self.current_gear + 1)

    def down_gear(self):
        self._set_gear(self.current_gear - 1)

    def ratio(self):
        return self.gear_ratios[self.current_gear - 1]


class Automatic(Manual):
    pass
























# class Automatic(Manual):
#     pass
#
#     def controller(self, speed):
#         gear_map = {
#             10: 1,
#             20: 2,
#             30: 3,
#             40: 4,
#             50: 5
#         }
#
#         self.set_gear(gear_map[speed])
#
#     def up(self):
#         self.gear += 1
#
#     def down(self):
#         self.gear -= 1
#
#
# class CVT(Transmission):
#     def __init__(self, brand):
#         super().__init__(brand)
#         # Или может тут ввести просто power или процентаж нагрузки на коробку
#         self.pulley_f = 0
#         self.pulley_s = 100
#
#     def set_pulley(self, pulley_f):
#         self.pulley_f = pulley_f
#         self.pulley_s = 100 - pulley_f
#
#     def controller(self, speed):
#         pulley_map = {
#             10: 20,
#             20: 40,
#             30: 60,
#             40: 80,
#             50: 100
#         }
#
#         self.set_pulley(pulley_map[speed])
