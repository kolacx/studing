from cars import Car
from drivers import Driver, ControlMT
from engines import Engine
from transmissions import MT, AT

if __name__ == "__main__":
    print("GOs")

    mt = MT([4.23, 2.53, 1.67, 1.23, 1, 0.83])
    at = AT([3.99, 2.65, 1.81, 1.39, 1.16, 1])
    engine = Engine(6500)
    car = Car(engine, mt)

    ctrl = ControlMT(mt)

    d = Driver(car, ctrl)
    d.drive()
