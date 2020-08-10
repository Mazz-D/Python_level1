"""
motorcycles =["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
print(f"\tA {too_expensive.upper()} is too expensive for me")

#Using the sort() method

cars = ["bwm", "audi", "benz", "toyota"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#the sort() and sort(reverse=True) permanently change the order of a list in alphabetical and reverse alphabetical order.

#Temporal list sorting using the sorted() function(it can accept the reserve=True argument too), does change the original order of things of the original variable

cars = ["toyota", "volks", "fiat", "tesla"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
"""