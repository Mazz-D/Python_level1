#Importing a single class
from Car import Car

my_new_car = Car("benz", "a6", 2017)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 24
my_new_car.read_odometer()