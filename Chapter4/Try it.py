"""
#Try it yourself
for numbers in range(1,20):
    print(numbers)

one_million = []
for numbers in range(1,1000000):
    one_million.append(numbers)
print(one_million)

for odd_numbers in range(1,21,3):
    print(odd_numbers)

cubes = []
for values in range(1,10):
    cube = values**3
    cubes.append(cube)
print(cubes)

#Try it yourself[slices()]

#tuple... an immutable(cannot change[constant]) list,apparently it shares the same characteristics with list, list uses square bracket while tuple uses parenthesis. to overwrite the values in a tuple, you have to change the values unlike the list, you can change valus by specifying the index place and chaging it.
#writing over a tuple

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
"""