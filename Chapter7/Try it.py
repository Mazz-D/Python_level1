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

#Multiples of Ten:
number = input("Give me a number and i will tell you if it is a multiple of ten: ")
number = int(number)
if number % 10 == 0 :
    print(f"{str(number)} is a multiple of 10")
else:
    print(str(number) + " is not a multiple of 10")

#7-4 Pizza Toppings:
prompt = "\nWhat is your order?: "
prompt += "\nAdd a new topping, until you enter 'quit': "

while True:
    pizza = input(prompt)
    if pizza == 'quit':
        print("Thank you for your order")
        break
    else:
        print(f" i will be adding {pizza} to your pizza order")

#7-5 Movie Tickets:
prompt = "\nHow old are you?: "
age = input(prompt)
age = int(age)
if age > 12 :
    print("The ticket is $15")
elif age < 3:
    print(f"The ticket is free")
else:
    print("The ticket is $10")

#7-6 and 7-7 will be attempted and attended to later

#7-8 and 7-9 Deli and No pastrami:
sandwich_orders = ["beef","pastrami", "fish", "carrot", "pastrami", "snail", "pastrami"]
finished_sandwiches = []
print("\nThe deli has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"\nI made your {order} sandwich")
    finished_sandwiches.append(order)
print(f"\nThe following sandwich has been made: ")
for finshed in finished_sandwiches:
    print(finshed.title())

#7-10 Dream vacation:
dream_places = {}
poll = True
while poll:
    name = input("\nWhat is your name? ")
    place = input("if you could visit one place in the world, where would you go? ")

    dream_places[name] = place
    another_place = input("\nDo you have some other place in mind? (yes/ no)")
    if another_place == "no":
        poll = False
print("\n--- Poll Results ---")
for name, place in dream_places.items():
    print(name + " would like to go to " + place + ".")
"""