# This shows how list is nest inside of a dictionary

favorite_language = {
    'abdul': ['python', 'sql'],
    'rahman': ['excel'],
    'kabia': ['java', 'tableau'],
    'ark': ['javascript', 'html'],
    }

for name, languages in favorite_language.items(): # loop through the dictionary and list to get the key and values
    print(f"\n{name.title()} favorite language(s) is/are:") # this prints the key and a statement

    # Get the values from the dictonary and the list
    for language in languages:
        print(language)

