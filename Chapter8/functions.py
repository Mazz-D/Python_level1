#parameters are made during function declaration/definiton, while arguments are the 'parameters' are the passed to the function when it is called for operation.
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