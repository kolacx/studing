from cars import Car
from factorys import CarCatalog, SimulatorMTFactory, SimulatorFactory, SimulatorATFactory, CarMTCarFactory
from loaders import ListLoader, LoadFromCSV, LoadFromJSON, LoadFromYAML, LoadFromXML
from transmissions import MT

db = ListLoader([
    LoadFromCSV('load_cars.csv', ';'),
    LoadFromJSON('load_cars.json'),
    LoadFromYAML('load_cars.yaml'),
    LoadFromXML('load_cars.xml')
]).load()

catalog = CarCatalog(db)


def do_sim(car):
    if isinstance(car.transmission, MT):
        factory = SimulatorMTFactory()
    else:
        factory = SimulatorATFactory()

    return factory.create_simulator(car)


if __name__ == "__main__":
    print('Test')

    car = catalog.get_by_code('ff_6500_MMT6_mt')
    simulator = do_sim(car)

    simulator.drive()
