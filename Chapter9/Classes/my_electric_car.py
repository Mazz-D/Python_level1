"""
from Car import ElectricCar
    
my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
#Overriding methods from a parent class: to override a method from a parent class, you will have to rewrite the method gotten from the parent, with the class specifying what you want it to do, the now method being specified in the child class will override the method functionality from the parent class
"""