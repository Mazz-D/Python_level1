#8-1 message:
def display_message(x):
    print("\nThis chapter is about functions")
    print("\nI hope you are ready for it " + x.title())
display_message("king")

#8-2 Favorite book:
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")

favorite_book("Lion king")