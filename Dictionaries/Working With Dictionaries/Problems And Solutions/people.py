# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

people = {
    'akabia': {
        'first_name': 'abdulrahaman',
        'last_name': 'kabia',
        'city': 'herndon',
    },

    'ajalloh': {
        'first_name': 'aminata',
        'last_name': 'kabia',
        'city': 'sterling',
    }
}

for users, information in people.items():
    print(f"\nUsername: {users}.") # this prints the user names in the dictionary with a space
    # this prints the users information and a tab
    print(f"\tFullname: {information['first_name'].title()} {information['last_name'].title()}.")
    print(f"\tLocation: {information['city'].title()}")