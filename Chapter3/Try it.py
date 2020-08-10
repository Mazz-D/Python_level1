"""
#Try it

people = ["John", "Peter", "Odias", "Eshovo", "Ehis"]
print(people)
print(len(people))
print(people[4])
message = (" I will like you to attend my family dinner")
print("Hello " + people[0].title() + message)
print("Hello " + people[1].lower() + message)
print("Hello " + people[2].upper() + message)
print("Hello " + people[3].lower() + message)
print("Hello " + people[4].title() + message)
print("Unfortunately " + people[3].title() + " can't attend")
del people[3]
people.insert(3, "greg")
print("Hello " + people[0].title() + message)
print("Hello " + people[1].lower() + message)
print("Hello " + people[2].upper() + message)
print("Hello " + people[3].lower() + message)
print("Hello " + people[4].title() + message)
print("Hey " + str(people) + " I found a bigger table" )
people.insert(0, "Elvis")
people.insert(3, "Muby")
people.append("Jack")
print(people)
print(len(people))
print("Hello " + people[0].title() + message)
print("Hello " + people[1].lower() + message)
print("Hello " + people[2].upper() + message)
print("Hello " + people[3].lower() + message)
print("Hello " + people[4].title() + message)
print("Hello " + people[5].title() + message)
print("Hello " + people[6].lower() + message)
print("Hello " + people[7].upper() + message)
print("Sorry " + str(people) + " I can only invite 2 people")
apology = " Sorry about the failed dinner"
people.pop(0)
people.pop(1)
people.pop(2)
people.pop(3)
print(people)

#Try it yourself
places = ["sweden", "estonia", "algeria", "rwanda", "australia", "japan"]
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
"""