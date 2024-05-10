class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    counter = 0

    # constructor
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # attributes/fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # methods
    def drive(self, city, speed):
        print(f'Car {self.model} is driving to {city} with speed {speed} km/h')

    def signal(self, number_of_times):
        print(f'Car {self.model} {' beep' * number_of_times}')
        # while number_of_times > 0:
        #     print('Beep')
        #     number_of_times -= 1


class Truck(Car):
    counter = 0

    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, weight, type_of):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg.')
        else:
            print(f'Cargo of {type_of} was successfully loaded into {self.model}')


number = 8
print(number)

print(f'Factory CAR produced: {Car.counter} cars.')

bmw_car = Car('BMW X7', 2020, 'red')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')

honda_car = Car(the_color='yellow', the_model='Honda Fit', penalties=900, the_year=2009)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')
# honda_car.color = 'green'
honda_car.change_color('green')
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} NEW COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')

bmw_car.drive('Osh', 100)
bmw_car.drive('Batken', 90)
honda_car.drive('Kant', 70)
honda_car.signal(3)

print(f'Factory CAR produced: {Car.counter} cars.')

boeing_plane = Plane('Boeing 747', 2022, 'white')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} COLOR: {boeing_plane.color}')

volvo_truck = Truck('Volvo 400', 2019,
                    'blue', 1200, 45000)
print(f'MODEL: {volvo_truck.model} YEAR: {volvo_truck.year} COLOR: {volvo_truck.color} '
      f'PENALTIES: {volvo_truck.penalties} LOAD CAPACITY: {volvo_truck.load_capacity}')
volvo_truck.load_cargo(50000, 'apples')
volvo_truck.load_cargo(30000, 'tomatoes')
volvo_truck.signal(1)
volvo_truck.drive('Tokmok', 80)

print(f'Factory TRUCK produced: {Truck.counter} trucks.')
