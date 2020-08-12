"""
# 8-1 message:
def display_message(x):
    print("\nThis chapter is about functions")
    print("\nI hope you are ready for it " + x.title())

display_message("king")

# 8-2 Favorite book:
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")

favorite_book("Lion king")

#8-3 T-shirt:
def make_shirt(shirt_size, shirt_text):
    input = "\nWhat size do you wear? "
    print(f"Your shirt size is {shirt_size} and your custom text is {shirt_text}")

make_shirt(9, "'Mangas are cool'") #--positional arguments
make_shirt(shirt_text="'I like anmine better'", shirt_size="XXL") #--keyword arguments

#8-4- Large Shirts:
def make_shirt(shirt_size="L", shirt_text="I love Python"):
    print(f"\nThis shirt is {shirt_size}, and {shirt_text}")
make_shirt()
make_shirt(shirt_size="M")
make_shirt(shirt_size="XL", shirt_text="Pyhthon is awesome")

#Cities:
def describe_cities(city_name, country="Nigeria"):
    print(f"\n{city_name.title()} is in {country.title()}")
describe_cities(city_name="Lagos")
describe_cities(city_name="Atlanta", country="America")
describe_cities(city_name="benin")
"""