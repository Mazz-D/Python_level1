""""
#A simple dictionary---alien.py

#alien_0 = {"color": "green", "points": 5}
#print(alien_0)
#alien_0["x_position"] = 0
#alien_0["y_position"] = 25
#print(alien_0)

#An Empty Dictionary
#alien_0 = {}

#alien_0["color"] = "green"
#alien_0["points"] = 5

#print(alien_0)

#modifying a dictionary
alien_0 = {"color": "green"}
#print("The alien is " + alien_0["color"] + ".")

alien_0["color"] = "yellow"
#print("The alien is now " + alien_0["color"] + ".")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
#move the the alien to the right
#Determine how far to move the alien based on its current speed
alien_speed = alien_0["speed"]
if alien_speed == "slow":
    x_increment = 1
elif alien_speed == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
#print("New x-position: " + str(alien_0["x_position"]))
#print(alien_0)
del(alien_0["speed"]) #del revomes the value permanently
#print(alien_0)

#Dictionary of similar objects
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
#for name, language in favorite_languages.items():
    #print(name.title() + "'s favorite language is " + language.title())
#print("Sarah's favorite language is " + favorite_languages["sarah"].title() + ".")
#looping through all the keys in a dictionary
friends = ["phil", "sarah"]
#for name in favorite_languages.keys():
    #print(name.title())
    #if name in friends:
        #print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
    #if "erin" not in favorite_languages.keys():
        #print("Erin, please take our poll!")
for name in sorted(favorite_languages.keys()):
    #print(name.title() +", thank you for taking the poll.")

#print("The following languages have been mentioned:")
for language in favorite_languages.values():
    #print(language.title())
#--- keys are values are methods used on dictionary lists, thay are also the what the contents of the dictionary are known as.
#to avoid repition while trying to get the values of a large set of dictionary entries, we use:
for language in set(favorite_languages.values()):
    #print(language.title())

#Try it yourself

person = {
    "first_name": "somine",
    "last_name": "rose",
    "age": 22,
    "city": "lagos"    
}

#print(person["first_name"].title())
#print(person["last_name"].title())
#print(person[str("age")])
#print(person["city"].title())

people_favorite_numbers = {
    "somine": 22,
    "ehis": 30,
    "oboro": 28,
    "mazz": 32,
    "ilo": 27,
}
for name, favNumber in people_favorite_numbers.items():
    #print("Key: " + key)
    #print("Value: " + str(value))
    #print(name.title() + " favorite number is " + str(favNumber))

#looping through a dictionary
#user_0 = {
    #"username": "efermi",
    #"first": "enrico",
    #"last": "fermi",
#}
#for key, value in user_0.items():
    #print("\nKey: " + key)
    #print("Value: " + value)

#NESTING
#A List of dictionaries
#ALIENS.PY

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    #print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#for alien in aliens[:5]:
    #print(alien)
#print("...")
#print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
#for alien in aliens[0:5]:
    #print(alien)

#A list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
#print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

#for topping in pizza['toppings']:
    #print("\t" + topping)

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby","go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    if languages:
        print(f"{name.title()} total languages are {len(languages)}")
    for language in languages:
        print("\t" + language.title())

#A dictionary in a dictionary

users = {
    "aeinstein": {
        "first":  "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print("\tFull name: " + full_name.title())
    print(f"\tLocation: {location.title()}")
"""