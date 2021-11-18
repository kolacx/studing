from abc import ABC, abstractmethod


class GearBox(ABC):
    def __init__(self):
        self._ratio = 0.0


class MT(GearBox):
    def __init__(self, ratio_list: list):
        super().__init__()
        self._ratio_list = ratio_list
        self._ratio_list.insert(0, 0.0)

    def set_gear(self, gear):
        self._ratio = self._ratio_list[int(gear)]

    def get_gear(self):
        return self._ratio_list.index(self._ratio)

    def gear_length(self):
        return len(self._ratio_list) - 1


class AT(MT):

    def up_set_gear(self):
        new_gear = self.get_gear() + 1

        if new_gear <= self.gear_length():
            self.set_gear(new_gear)

    def down_set_gear(self):
        new_gear = self.get_gear() - 1

        if new_gear >= 1:
            self.set_gear(new_gear)
