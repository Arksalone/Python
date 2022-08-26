# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

# information about childhood friend
childhood_friend = {
    'first_name': 'alusine',
    'middle_name': 'samuel',
    'last_name': 'bangura',
    'age': 32,
    'city': 'freetown',
    }

# each piece of information stored for my friend
print(f"{childhood_friend['first_name'].title()} \n{childhood_friend['middle_name'].title()} \n{childhood_friend['last_name'].title()} \n{childhood_friend['age']} \n{childhood_friend['city'].title()}")