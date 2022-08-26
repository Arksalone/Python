# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

# favorite numbers of friends
favorite_number = {
    'halley': 125,
    'abdul': 400,
    'rahman': 250,
    'aminata': 100,
    'kabia': 300,
    }

for person, info in favorite_number.items(): # loop through the items and print each person name in title case and their favorite number
    print(f"{person.title()} favorite number is {info}.")


# Same output but without for loop
print() # this prints a blank space
print("Same problem without for loop!") # header statement
print() # this prints a blank space

# favorite numbers of friends
favorite_number = {
    'halley': 125,
    'abdul': 400,
    'rahman': 250,
    'aminata': 100,
    'kabia': 300,
    }

print(f"Halley's favorite number is {favorite_number['halley']}.")
print(f"Abdul's favorite number is {favorite_number['abdul']}.")
print(f"Rahman's favorite number is {favorite_number['rahman']}.")
print(f"Aminata's favorite number is {favorite_number['aminata']}.")
print(f"Kabia's favorite number is {favorite_number['kabia']}.")