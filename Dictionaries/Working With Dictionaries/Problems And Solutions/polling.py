# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

# people and their favorite language
favorite_language = {
    'abdul': 'python',
    'rahman': 'sql',
    'kabia': 'excel',
    'arksalone': 'amazon aws',
    }

# list of people that have taken the poll and those that are not
friends = ['ark', 'aminata', 'abdulrahman', 'abduL', 'RAHMAN', 'KAbia']

# covert to friends list to lower case
friends_lower = [friend.lower() for friend in friends]

for names in friends_lower: # for names match in the frien list
    if names in favorite_language:
        print(f"Hi {names.title()}, you have already taken the poll! Thank you!")
    else:
        print(f"Hi {names.title()}, please take the poll!")
