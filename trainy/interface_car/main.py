from cars import Car
from drivers import Driver
from engines import Engine
from transmissions import MT, AT

if __name__ == "__main__":
    print("GO")

    mt = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83])
    at = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1])
    engine = Engine(6500)
    car = Car(engine, mt)

    d = Driver(car)
    d.drive()
