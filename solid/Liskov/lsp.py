from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fly(self):
        pass


class Duck(Bird):
    def fly(self):
        print('Duck - fly')


class Chiken(Bird):
    def fly(self):
        print('Chiken dont fly')


# +++++++++++++++++++++++++++++++

class InterfaceForAbstruct(ABC):
    def __init__(self, name):
        self.name = name


class FlyBird(InterfaceForAbstruct):

    @abstractmethod
    def fly(self):
        pass


class WalkBird(InterfaceForAbstruct):

    @abstractmethod
    def walk_bird(self):
        pass


class Duck2(FlyBird):
    def fly(self):
        print('Fly1')


class WalkB(WalkBird):
    def walk_bird(self):
        print('Walk2')


if __name__ == "__main__":
    f = Duck2('Duck')
    w = WalkB('Wal')
    #
    f.fly()
    w.walk_bird()