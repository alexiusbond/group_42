class Employee:
    def __init__(self, first_name, last_name, salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary

    def __str__(self):
        return f'{self.__first_name} {self.__last_name} {self.__salary}'


# print(__name__)
if __name__ == '__main__':
    employee = Employee('John', 'Smith', 5000)
    print(employee)
