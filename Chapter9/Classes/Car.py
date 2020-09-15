class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #setting a default value

    def get_descriptive_name(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it")

    def update_odometer(self, mileage): #modifying an attribute value through a method
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an odometer")

    def increment_odometer(self, miles): #incrementing an attribute value through a method
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {str(self.battery_size)}-kWh battery")

    def get_range(self):
        if self.battery_size ==70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f"This car can go approximately {str(range)}"
        message += f" miles on full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
"""    
my_used_car = Car("audi", "q7", 2017)
print(my_used_car.descriptive_name())

my_used_car.update_odometer(24000)
my_used_car.read_odometer()

my_used_car.increment_odometer(500)
my_used_car.read_odometer()
"""