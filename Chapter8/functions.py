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
"""
#Using a function on a while loop
