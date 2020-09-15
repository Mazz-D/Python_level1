
#Importing multiple classes from module
from Car import Car, ElectricCar

my_bettle = Car("volkswagen", "bettle", 2016)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roadstar", 2016)
print(my_tesla.get_descriptive_name())

#importing an entire module

import Car
my_bettle = Car.Car("volkswagen", "bettle", 2016)
print(my_bettle.get_descriptive_name())

my_tesla = Car.ElectricCar("tesla", "roadstar", 2016)
print(my_tesla.get_descriptive_name())