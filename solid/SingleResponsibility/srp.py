class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.tank = 0

    def tank_car(self, litre):
        self.tank = litre


class CarMoves:

    def move_forward(self, car):
        print(car.brand, 'Move Forward')

    def move_backward(self, car):
        print(car.brand, 'Move Backward')


class GoToCar:

    def go_to_garage(self, car):
        print(car.brand, 'Moved to garage')

    def go_to_service(self, car):
        print(car.brand, 'Moved to service')
