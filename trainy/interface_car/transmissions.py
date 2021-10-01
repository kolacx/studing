from abc import ABC, abstractmethod


class GearBox(ABC):
    def __init__(self):
        self.ratio = 0

    @abstractmethod
    def get_len_gearbox(self):
        pass

    @abstractmethod
    def set_gear(self, gear):
        pass

    @abstractmethod
    def current_gear(self):
        pass


class MT(GearBox):
    def __init__(self, ratio_list: list):
        super().__init__()
        self.ratio_list = ratio_list

    def set_gear(self, gear):
        self.ratio = self.ratio_list[int(gear) - 1]

    def get_len_gearbox(self):
        return len(self.ratio_list)

    def current_gear(self):
        if self.ratio == 0:
            return 0
        else:
            return self.ratio_list.index(self.ratio) + 1


class AT(MT):
    pass
