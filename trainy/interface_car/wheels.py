from abc import ABC, abstractmethod


class Tire:
    def __init__(self, brand, radius, width, height):
        self.brand = brand
        self.radius = radius
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Brand: {self.brand} - R{self.radius} {self.width}/{self.height}'


class Wheel:
    def __init__(self, brand, radius, width, tire: Tire):
        self.brand = brand
        self.radius = radius
        self.width = width
        self.tire = tire

    def __repr__(self):
        return f'Brand: {self.brand} - R{self.radius} {self.width}J'
