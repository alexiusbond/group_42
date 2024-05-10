class Contact:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Animal:
    def __init__(self, name, age, contact):
        self.__name = name
        if type(age) == int and age > 0:
            self.__age = age
        if type(contact) == Contact:
            self.__contact = contact
        self.__was_born()

    def __was_born(self):
        print(f"Animal {self.__name} was born")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if type(new_age) == int and new_age > 0:
            self.__age = new_age
        else:
            raise ValueError('Age must be a positive number')

    def info(self):
        return (f'{self.__name} is {self.__age} years old. '
                f'Birth year is {2024 - self.__age} '
                f'Contact Info: {self.__contact.city}, {self.__contact.street} {self.__contact.number}')

    def speak(self):
        raise NotImplementedError('You must implement method speak')

class Fish(Animal):
    def __init__(self, name, age, contact):
        super(Fish, self).__init__(name, age, contact)

    def speak(self):
        pass

class Cat(Animal):
    def __init__(self, name, age, contact):
        # super().__init__(name, age)
        super(Cat, self).__init__(name, age, contact)

    def speak(self):
        print('Myauu')


class Dog(Animal):
    def __init__(self, name, age, commands, contact):
        super(Dog, self).__init__(name, age, contact)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f'\nCommands: {self.__commands}'

    def speak(self):
        print('Gav')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contact):
        super(FightingDog, self).__init__(name, age, commands, contact)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f'\nWins: {self.__wins}'

    def speak(self):
        print('Rrrrr gav')


# some_animal = Animal(name='Anim', age=2)
# some_animal.set_age(3)
# some_animal.set_name('Bob')
# print(some_animal.get_name())
# print(some_animal.info())

contact_1 = Contact('Bishkek', 'Isanova', 8)

cat = Cat('Tom', 5, contact_1)
# print(cat.info())

dog = Dog('Snoopy', 1, ['sit', 'run'], contact_1)
dog.commands = ['sit', 'run', 'bark']
# print(dog.commands)
# print(dog.info())

# contact_2 = Contact('Osh', 'Lenina', 11)
#         a = b
fighting_dog = FightingDog('Reks', 2, ['fight'], 10,
                           Contact('Osh', 'Lenina', 11))
# print(fighting_dog.info())

# contact_1.number = 33
# print(dog.info())
# print(cat.info())

fish = Fish('Nemo', 3, contact_1)

animals_list = [cat, fish, dog, fighting_dog]
for animal in animals_list:
    print(animal.info())
    animal.speak()
