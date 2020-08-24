"""
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over")

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car("audi", "a6", 2016)
print(my_new_car.get_descriptive_name())
"""
#setting a default value for an attribute
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

my_new_car = Car("audi", "a6", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#Modifying an attribute value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Modifying an attribute's value through a method
my_new_car.update_odometer(23)
my_new_car.update_odometer(20)
my_new_car.read_odometer()
my_new_car.update_odometer(18)
my_new_car.read_odometer()

