"""
# 8-1 message:
def display_message(x):
    print("\nThis chapter is about functions")
    print("\nI hope you are ready for it " + x.title())

display_message("king")

# 8-2 Favorite book:
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")

favorite_book("Lion king")

#8-3 T-shirt:
def make_shirt(shirt_size, shirt_text):
    input = "\nWhat size do you wear? "
    print(f"Your shirt size is {shirt_size} and your custom text is {shirt_text}")

make_shirt(9, "'Mangas are cool'") #--positional arguments
make_shirt(shirt_text="'I like anmine better'", shirt_size="XXL") #--keyword arguments

#8-4- Large Shirts:
def make_shirt(shirt_size="L", shirt_text="I love Python"):
    print(f"\nThis shirt is {shirt_size}, and {shirt_text}")
make_shirt()
make_shirt(shirt_size="M")
make_shirt(shirt_size="XL", shirt_text="Pyhthon is awesome")

#8-5 Cities:
def describe_cities(city_name, country="Nigeria"):
    print(f"\n{city_name.title()} is in {country.title()}")
describe_cities(city_name="Lagos")
describe_cities(city_name="Atlanta", country="America")
describe_cities(city_name="benin")

#City names:
def city_country(city, country):
    city_country = f"{city},{country}"
    return city_country.title()

location = city_country("agege", "lagos")
print(location)
location_2 = city_country("jos", "pleatue")
print(location_2)

#8-7 Album:
def make_album(artist_name, artist_album, album_tracks="", genre=""):
    artist = {"artist": artist_name, "album": artist_album}
    if album_tracks:
        artist["tracks"] = album_tracks
    if genre:
        artist["genre"] = genre
    return artist
musician = make_album("jimi hendrix", "flower", album_tracks= 20, genre="rock")
print(musician)
"""
#8-8 user albums:--- revisit later
def make_album(artist_name, artist_album):
    artist = f"Artist Name: {artist_name} \nArtistalbum: {artist_album}"
    return artist.title()
while True:
    print("\nPlease an album artist: ")
    print("Enter album title: ")
    print("\nEnter 'q' when done")
        
    artist_name = input("Artist name: ")
    if artist_name == "q":
        break
    artist_album = input("Artist album: ")
    if artist_album == "q":
        break
artist = make_album(artist_name, artist_album)
print(artist)