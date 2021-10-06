from abc import ABC, abstractmethod


class GearBox(ABC):
    def __init__(self):
        self.ratio = 0.0

    def get_ratio(self):
        return self.ratio


class MT(GearBox):
    def __init__(self, ratio_list: list):
        super().__init__()
        self.ratio_list = ratio_list
        self.gear_len = len(ratio_list)

    def set_gear(self, gear):
        print(f'TRANSMISSION MT - set_gear {gear}')
        self.ratio = self.ratio_list[int(gear) - 1]

    def get_len_gearbox(self):
        return self.gear_len

    def get_current_gear(self):
        if self.ratio == 0:
            return 0
        else:
            return self.ratio_list.index(self.ratio) + 1


class AT(MT):
    pass
