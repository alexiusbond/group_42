from random import randint as generate_number, choice

from termcolor import cprint

import utilities.calculator as calc
from utilities.person import Employee
import emoji
from decouple import config

print(generate_number(1, 6))
print(choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))

print(calc.multiply(2, 5))

my_employee = Employee('Jim', 'Black', 4500)
print(my_employee)

cprint("Hello, World!", "green", "on_red")

print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))
commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)
