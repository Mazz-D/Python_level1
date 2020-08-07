#using for loop
"""
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
    print("Thank you, everyone. That was a great magic show!")
"""
#Try it yourself(for loop)
"""
favorite_pizza = ["pineapple", "pepperoni", "mushroom"]
for pizza in favorite_pizza:
    print(pizza)
    print(f"I like {pizza} pizza \n")

print(f"I really love pizza")
"""
""""
animals = ["cat", "dog", "parrot"]
for pet in animals:
    print(pet)
    print("A " + pet + " will make a great pet" + "\n")

print("any of these animals will make a great pet")
"""
#Making Numerical lists
"""
for values in range(1,8):
    print(values)
numbers = list(range(3,10))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)
#list comprehensiom
squares = [value**2 for value in range(1,11)]
print(squares)
"""

#Try it yourself
#for numbers in range(1,20):
 #   print(numbers)
"""
one_million = []
for numbers in range(1,1000000):
    one_million.append(numbers)
print(one_million)
"""

#for odd_numbers in range(1,21,3):
 #   print(odd_numbers)
"""
cubes = []
for values in range(1,10):
    cube = values**3
    cubes.append(cube)
print(cubes)

#In list comprehension
cubes = [value**3 for value in range(1,10)]
print(cubes)
"""
"""
#Using slice()
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[-3:])

players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three players for my team:")
for player in players[:3]:
    print(player.title())
"""
#copying a list
"""
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

friend_foods.append("kola")
my_foods.append("igboo")
print("My favorite food are:")
print(my_foods)

print("\nMy friends favorite food are:")
print(friend_foods)
"""
#Try it yourself[slices()]

#tuple... an immutable(cannot change[constant]) list,apparently it shares the same characteristics with list, list uses square bracket while tuple uses parenthesis. to overwrite the values in a tuple, you have to change the values unlike the list, you can change valus by specifying the index place and chaging it.
#writing over a tuple
"""
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#Try it
basic_foods = ("pap", "akara", "pizza", "orange", "apple")
for food in basic_foods:
    print(food.title())

#this below will produce an error since it's not a list
#basic_foods[3] = ("corn")
#print(basic_foods)

basic_foods = ("goat meat", "akara", "beans", "orange", "apple")
for new_food in basic_foods:
    print(new_food.title())
"""
