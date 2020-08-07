"""
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())    

#using tuple
cars = ("audi", "bmw", "subaru", "toyota")
for car in cars:
    if car == "audi":
        print(car.upper())

banned_user = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_user:
    print(user.title() + ", you can post a response if you wish")
    print(f"{user.upper()} , you can post a response if you wish")

#try it yourself
anime = ["naruto", "one piece", "bleach"]
print(f"Is {anime[0]} == 'naruto'? i predict True ")
print (anime[0] == "naruto")
"""
"""
#if statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registred yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
 
#if-elif-else chain
age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 50
print("Your admission fee is $" + str(price))

#Try it yourself
alien_color = ["green", "yellow", "red"]
if "green" in alien_color:
    print("You just earned 5 points")
if "yellow" in alien_color:
    print("You can try again")
if "blue" in alien_color:
    print("The game is just starting")

alien_color2 = ["blue"]
if "green" in alien_color2:
    print("You earn 5 points for shooting the alien down")
if "green" not in alien_color2:
    print("You just earned 10points")
if "green" in alien_color2:
    print("You earned 5 points for shooting the alien down")
elif
else:
    print("you need to try harder")

#Using multiple Lists
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print(f"\nFinished making your pizza")
"""

#if value is  and not in a list
#requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
#if "mushrooms" in requested_toppings:
#    print("Adding mushrooms.")
#if "pepperoni" in requested_toppings:
#    print("Adding pepperoni.")
#if "extra cheese" in requested_toppings:
#    print("Adding extra cheese.")
#    print("\nFinished making your pizza!")

#for requested_topping in requested_toppings:
#    if requested_topping == "green peppers":
#        print("Sorry we are out of green peppers right now")
#    else:
#        print("Adding " + requested_topping + ".")
#
#print("\nFinished making your pizza")

#requested_toppings = []
#if requested_toppings:
#    for requested_topping in requested_toppings:
#        print("Adding " + requested_topping + ".")
#    print("\nFinished making your pizza!")
#else:
#print("Are you sure you want a plain pizza?")
#Try it yourself
usernames = ["user1", "user2", "user3", "user4", "admin"]
