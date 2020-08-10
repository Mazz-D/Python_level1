"""
message = input("Tell me something and I will repeat it back to you:")
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is you name: "
name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
print(age)

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 40:
    print("\nYou're tall enough to ride")
else:
    print("\nYou'll be able to ride when you're a bit taller")

number = input("Enter a number and i will tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {str(number)} is even")
else:
    print("\nThe number " + str(number) + " is odd")


#Introducing while loops
current_number = 1 
while current_number <= 5:
    print(current_number)
    current_number += 1

#making a choice on when to quit

prompt = "\nTell me something, and i will repeat it back to you: "
prompt += "\nEnter'quit' to end the program. "
#Using a flag
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#using break to exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

#using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

str4 = "world"
new = str4[:-1]
print(new)

#using a while loop with list and dictionaries
# a for loop is effective for looping through a list but don't shouldn't modify it, instead use a while loop while working through it, while loop allows you to collect, store and organize lots of input to examine and report on later.

#Moving items from one list to another

unconfirmed_users = ["alice", "brain", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Removing all instances of specific values from a list
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)
"""
#Filling a dictionary with user input
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb  someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")