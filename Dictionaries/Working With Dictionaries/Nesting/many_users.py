# This demonstrate how dictonaries are nested inside of a dictonary

users = {
    'akabia': {
        'first_name': 'abdulrahman',
        'last_name': 'kabia',
        'location': 'freetown',
    },

    'ajalloh': {
        'first_name': 'aminata',
        'last_name': 'jalloh',
        'location': 'sierra leone',
    }

}

for username, information in users.items():
    print(f"\nUserame: {username}") # this prints the users nicknames

    # extracting the users fullname and location
    print(f"\tFullname: {information['first_name'].title()} {information['last_name'].title()}.")
    print(f"\tLocation: {information['location'].title()}.")
