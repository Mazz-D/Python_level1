"""
#parameters are made during function declaration/definiton, while arguments are the 'parameters' passed to the function when it is called for operation.
#Positional arguments
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()} ")

describe_pet("hamster", "harry")
describe_pet("dog", "willie")
#order matters when in positional arguments
#Keyword Arguments: A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion.
#Rewriting the above example using keyword arguments
describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")

#default values:
#in default values, the parameters are arranged that the default values are placed last in the parenthesis.
def describe_pet(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet(pet_name="willie")

#Return values:
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)
anime = get_formatted_name("uzumaki", "naruto")
print(anime)

#making an argument optional
def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("john", "lee", "hooker")
print(musician)
#making an argument optional require the parameter to be made an empty string during function decalration...
def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)

musician = get_formatted_name("john", "hooker", "lee")
print(musician)

#returning dictionary
def build_person(first_name, last_name):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person("jimi", "hendrix")
print(musician)

#extending a function with a dictionary in it
def build_person(first_name, last_name, age=""):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person
musician = build_person("jimi", "hendrix", age=27)
print(musician)

#Using a function on a while loop
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell us your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break

formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")

#Passing a list
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ["hannah", "ty", "margot"]
greet_users(usernames)

#modifying a list in a function
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Preventing a function from modifying a list
#to prevent a function from modify or empyting an original list, the list can be copied with the list copy notation[:]

#Passing an Arbitrary number of arguments
#This is the concept were a function doesn't know how many possible arguments it will get during its function call, and when more arguments are added to the function, they are stored in a tuple kind of list

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

#Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    print(f"\nMaking a {str(size)}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,"pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

#Using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)
#in summary of the abitrary passing of arguments, the single asterik and double asterik used on parameters during definiton of the funtion are used to represent a tuple and a dictionary respectively.
"""
#Storing functions in Modules
