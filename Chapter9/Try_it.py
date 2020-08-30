"""
#9-1 Restuarant and 9-4 Number served:
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}")
        print(f"We offer: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business")

    def set_number_served(self, customers_number):
        self.number_served = customers_number
        print(f"The {self.restaurant_name} restuarant has served {str(restaurant.number_served)} customers")

    def increment_number_served(self, number_served):
        self.number_served += number_served
        print(f"The {self.restaurant_name} restuarant has served {str(restaurant.number_served)} more customers")

restaurant = Restaurant("KFC", "chicken")
print(restaurant.describe_restaurant())
restaurant.set_number_served(245)
restaurant.set_number_served(50)
restaurant.increment_number_served(3)

#9-2 Three restaurant:
restaurant_2 = Restaurant("Yahuza", "Suya")
print(restaurant_2.describe_restaurant())
restaurant_2.customers_served(10
)

restaurant_3 = Restaurant("Mama put", "eba,rice")
print(restaurant_3.describe_restaurant())
"""
"""
#9-3 Users and 9-5 Login attempts:
class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempt = 0
    
    def name_summary(self):
        print("You filled in the following:")
        print(f"{self.first_name}, {self.last_name}, {str(self.age)}, {self.sex}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome to your profile")

    def increment_login_attempt(self, login_attempt ):
        self.login_attempt += 1
        print(str(self.login_attempt))

    def reset_login_attempts(self):
        self.login_attempt = 0
        print((self.login_attempt))

user_1 = User("king", "luff", 20, "M")
user_1.name_summary()
user_1.greet_user()
user_1.increment_login_attempt(0)
user_1.increment_login_attempt(0)
user_1.increment_login_attempt(0)
user_1.increment_login_attempt(0)

user_1.reset_login_attempts()
user_1.increment_login_attempt(0)
"""

#9-6 Ice cream stand:
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

class IceCreamStand():
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors[""]

    def display_flavors(self):
        print(f"These are the icecream flavors avaliable:")
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand("king", "icecream")
ice_cream_stand.display_flavors()