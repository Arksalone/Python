# my friends and their favorite language
favorite_language = {
    'abdul': 'python',
    'rahman': 'sql',
    'kabia': 'excel',
    'ark': 'javascript',
    }
# list of friends to check on
friends = ['abdul', 'aRK']
friends_lower = [friend.lower() for friend in friends] # convert the list to a lowercase

for names, language in sorted(favorite_language.items()):
    print(f"{names.title()}")

    # check the list of friends to see who likes what
    if names.lower() in friends_lower:
        print(f"Hi {names.title()}, why do you like {language}?")
    else:
        print(f"Hi {names.title()}, you are not in the list!")