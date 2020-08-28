class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #setting a default value

    def descriptive_name(self):
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
    
my_used_car = Car("audi", "q7", 2017)
print(my_used_car.descriptive_name())

my_used_car.update_odometer(24000)
my_used_car.read_odometer()

my_used_car.increment_odometer(500)
my_used_car.read_odometer()
