"""
#7-1 Rental Car:
car = input("What type of car are you looking for to rent? ")
print(f"let me see if i can find you a {car}")

#7-2 Restuarant Seating:
dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)
if dinner_group >=8 :
    print("I'm sorry, please wait a bit longer")
else:
    print("We have a table for you")

"""

#Multiples of Ten:
number = input("Give me a number and i will tell you if it is a multiple of ten: ")
number = int(number)
if number % 10 == 0 :
    print(f"{str(number)} is a multiple of 10")
else:
    print(str(number) + " is not a multiple of 10")
