from abc import ABC, abstractmethod


class GearBox(ABC):
    def __init__(self):
        self.ratio = 0.0


class MT(GearBox):
    def __init__(self, ratio_list: list):
        super().__init__()
        self.ratio_list = ratio_list
        self.ratio_list.insert(0, 0.0)

    def set_gear(self, gear):
        self.ratio = self.ratio_list[int(gear)]

    def get_current_gear(self):
        return self.ratio_list.index(self.ratio)

    def gear_length(self):
        return len(self.ratio_list) - 1


class AT(MT):
    pass
