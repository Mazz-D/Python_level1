"""
#in dictionary, there are these methods:
#items() to sort through the whole items
#keys() to check for the key values
#values() to loop through and check values
#set() function to make sure there aren't repitition in a large list
#sorted() to arrange them

#6-5
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "niger": "nigeria",
}
for river, place in rivers.items():
    print(f"the {river.title()} runs through {place.title()}")
    print("The " + river.title() + " runs through " + place.title())

print("The Names of all the rivers:")
for river in sorted(rivers.keys()):
    print(river.title())

print("The names of all the countries rivers are located:")
for place in rivers.values():
    print(place.title())

#6-6
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
to_take = ["jen", "ehis", "sarah", "jon"]
for name in favorite_languages.keys():
    if name in to_take:
        #print(name.title())
        print(f"Thank you {name.title()} for responding")
    else:
        print(f"{name.title()} please, make sure to take the poll")

#6-7
#this is how to dictonaries are used in a list
person_1 = {
    "first_name": "somine",
    "last_name": "rose",
    "age": 22,
    "city": "lagos",
    }
person_2 = {
        "first_name": "ehis",
        "last_name": "chill",
        "age": 29,
        "city": "benin",
    }
person_3 = {
        "first_name": "joe",
        "last_name": "bill",
        "age": 32,
        "city": "oyo"
    }
people = [person_1, person_2, person_3]
for name in people:
    print("\nThe names of the people in this list are: ")
    full_name = name["first_name"] + " " + name["last_name"]
    age = name["age"]
    city = name["city"]
    print(f"\t{full_name.title()}")
    print(f"\t{str(age)}")
    print(f"\t{city.title()}")


#6-8
luffy = {
    "animal_type": "dog",
    "owner": "somine"
}
zoro = {
    "animal_type": "cat",
    "owner": "bill",
}
nami = {
    "animal_type": "parrot",
    "owner": "law",
}
chopa = {
    "animal_type": "monkey",
    "owner": "king"
}

pets = [luffy,zoro, nami,chopa]

for animal in pets:
    print("\nThis is the info for each pet: ")
    pet_type = animal["animal_type"]
    pet_owner = animal["owner"]
    print(f"Pet-Type:{pet_type.title()}")
    print("Pet-Owner:" + pet_owner.title())

#6-9
favorite_places = {
    
}
"""