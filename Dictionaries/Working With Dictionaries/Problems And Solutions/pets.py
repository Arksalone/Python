# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.

# dictionaries containing pets information and owners stored in a list
pets = [
    {
    'name': 'bingo',
    'animal': 'dog',
    'owner': 'halley',
    'weight': 23,
    'food': 'meat',
    },

    {
    'name': 'sparrow',
    'animal': 'parrot',
    'owner': 'abdul',
    'weight': 12,
    'food': 'fish',
    },

    {
    'name': 'samson',
    'animal': 'lion',
    'owner': 'ark',
    'weight': 17,
    'food': 'meat',
    }

    ]

for pet in pets: # loop through the list to get every information about the pets
    print(f"{pet['name'].title()} the {pet['animal'].title()} is own by {pet['owner'].title()}, weighs {pet['weight']} and eat {pet['food']}.")