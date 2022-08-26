# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

# favorite places of friens stored in a dictionary
favorite_places = {
    'abdul': {
        'vacation_spot_one': 'santorini',
        'vacation_spot_two': 'maldives',
        'vacation_spot_three': 'freetown',
    },

    'rahman': {
        'vacation_spot_one': 'dubai',
        'vacation_spot_two': 'paris',
        'vacation_spot_three': 'berlin',
    },

    'ark': {
        'vacation_spot_one': 'new york',
        'vacation_spot_two': 'washington dc',
        'vacation_spot_three': 'tempe',
    },
}

# loop through the dictonary to print each friends name and their favorite places
for friends, vacation_spots in favorite_places.items():
    print(f"\nFriend: {friends.title()}.")
    print(f"\tFavorite places: {vacation_spots['vacation_spot_one'].title()}, {vacation_spots['vacation_spot_two'].title()}, {vacation_spots['vacation_spot_three'].title()}.")