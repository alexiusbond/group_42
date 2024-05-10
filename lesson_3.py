from enum import Enum


class Color(Enum):
    RED = '\033[31m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'


class Drawable:

    def draw(self, emoji):
        print(emoji)


class MusicPlayable:
    # def __init__(self):
    #     pass

    def play_music(self, song):
        print(f'Device {self.model} playing song {song}')

    def stop_music(self):
        print(f'Device {self.model} stopped music')


class SmartPhone(MusicPlayable, Drawable):
    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        return self.__model


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if type(color) == Color:
            self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return (f'Model: {self.__model}, Year: {self.__year}, '
                f'Color: {self.__color.value}{self.__color.name}' + '\033[0m')

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __ge__(self, other):
        return self.__year >= other.__year


class FuelCar(Car):
    total_fuel = 0

    @staticmethod
    def get_fuel_type():
        return 'AI 95'

    @classmethod
    def buy_fuel(cls, amount):
        cls.total_fuel += amount

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model, year, color)
        # super(FuelCar, self).__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def __str__(self):
        return super().__str__() + f', Fuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel')


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by electricity')

    def __str__(self):
        return super().__str__() + f', Battery: {self.__battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


# some_car = Car('Ford Focus', '2009', 'Black')
# print(some_car)

FuelCar.buy_fuel(1000)

civic_car = FuelCar('Honda Civic', 2019, Color.BLUE, 70)
print(civic_car)

tesla_car = ElectricCar('Tesla Model X', 2022, Color.RED, 25000)
print(tesla_car)

prius_car = HybridCar('Toyota Prius', 2021, Color.GREEN, 60, 15000)
print(prius_car)

prius_car.drive()
print(HybridCar.mro())

number_1, number_2 = 5, 8
fruit_1, fruit_2 = 'apple', 'banana'
print(f'Number one is greater than number two: {number_1 > number_2}')
print(f'Number two is greater than number one: {number_2 > number_1}')
print(f'Civic is better than Prius: {civic_car > prius_car}')
print(f'Civic is not the same with Prius: {civic_car != prius_car}')

print(number_1 + number_2)
print(fruit_1 + fruit_2)
print(civic_car + prius_car)

print(f'FACTORY FUEL_CAR has {FuelCar.total_fuel} ({FuelCar.get_fuel_type()}) litters of fuel.')

tesla_car.play_music('Best song')
civic_car.play_music('Song 1')

samsung = SmartPhone('Samsung 12')
samsung.play_music('My Song')
prius_car.draw('🚗')
samsung.draw('📱')

if tesla_car.model == 'Tesla Model-X':
    print('This car is cool!')

if tesla_car.color == Color.RED:
    print('This car is beautiful!')