from abc import ABC, abstractmethod


class GearBox(ABC):
    def __init__(self):
        self.ratio = 0.0

    # def get_ratio(self):
    #     return self.ratio


class MT(GearBox):
    def __init__(self, ratio_list: list):
        super().__init__()
        self.ratio_list = ratio_list

    def set_gear(self, gear):
        self.ratio = self.ratio_list[gear - 1]


class AT(MT):
    pass
