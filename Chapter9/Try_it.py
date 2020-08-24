
#9-1 Restuarant:
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}")
        print(f"We offer: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business")
    
restaurant = Restaurant("KFC", "chicken")
print(restaurant.describe_restaurant())

#9-2 Three restaurant:
restaurant_2 = Restaurant("Yahuza", "Suya")
print(restaurant_2.describe_restaurant())

restaurant_3 = Restaurant("Mama put", "eba,rice")
print(restaurant_3.describe_restaurant())

#9-3 Users:
class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    
    def name_sumarry(self):
        print("You filled in the following:")
        print(f"\n{self.first_name} \n{self.last_name} \n{str(self.age)} \n{self.sex}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome")

user_1 = User("king", "luff", 20, "M")
print(user_1.name_sumarry())
print(user_1.greet_user())