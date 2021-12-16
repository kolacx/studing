from cars import Car, CarAT, CarMT
from factorys import CarCatalog, SimulatorMTFactory, SimulatorFactory, SimulatorATFactory, CarMTCarFactory
from loaders import ListLoader, LoadFromCSV, LoadFromJSON, LoadFromYAML, LoadFromXML
from transmissions import MT, AT

db = ListLoader([
    LoadFromCSV('load_cars.csv', ';'),
    LoadFromJSON('load_cars.json'),
    LoadFromYAML('load_cars.yaml'),
    LoadFromXML('load_cars.xml')
]).load()


def create_simulator_by_car(car: [CarMT, CarAT]):

    if type(car.transmission) == MT:
        factory = SimulatorMTFactory()
    elif type(car.transmission) == AT:
        factory = SimulatorATFactory()
    else:
        raise TypeError

    return factory.create_simulator(car)


if __name__ == "__main__":
    print('Test')

    catalog = CarCatalog(db)

    max_len_key = max(catalog.db.keys(), key=len)

    for i, (k, v) in enumerate(catalog.db.items()):
        space = len(max_len_key) - len(k)
        print(i, k, ' ' * space, v)

    id_car = int(input('Number: '))
    car_code = list(catalog.db.keys())[id_car]

    # ====== ||| ======

    car = catalog.get_by_code(car_code)
    simulator = create_simulator_by_car(car)

    simulator.drive()
