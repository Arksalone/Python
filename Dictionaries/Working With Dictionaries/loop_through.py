# loop through a dictionary
# information of a person in a website

person_info = {
    'first_name': 'abdul',
    'middle_name': 'rahman',
    'last_name': 'kabia',
    }

# loop through the information
for person, info in person_info.items():
    print(f"{person}") # this prints the keys in the dictionary
    print(f"{info.title()}\n") # this prints the values
    print(f"{person}: {info.title()}.") # this prints both the keys and values