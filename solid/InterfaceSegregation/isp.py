from abc import ABC, abstractmethod


class InterfaceSmartphone(ABC):
    @abstractmethod
    def call(self):
        pass

    def internet(self):
        pass

    def sms(self):
        pass


class InterfaceStacionar(ABC):
    @abstractmethod
    def call(self):
        pass


class Smartphone(InterfaceSmartphone):
    def __init__(self, name):
        self.name = name

    def call(self):
        print('Calling')

    def internet(self):
        print('Internet')

    def sms(self):
        print('sms')


class Stacionar(InterfaceStacionar):
    def __init__(self, name):
        self.name = name

    def call(self):
        print('Calling')
