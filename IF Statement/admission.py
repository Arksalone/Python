# Admission for anyone under age 4 is free.
# • Admission for anyone between the ages of 4 and 18 is $5.
# • Admission for anyone age 18 or older is $10.

# Ask attendees to enter their ages
attendees = int(input('What is your age, please? '))

# using if statement to check who should pay upon entry and who should enter free
if attendees < 4:
    print(f"Because you are {attendees}, you won't have to pay!")
elif (attendees >= 4) and (attendees < 18):
    print(f"Because you are {attendees}, you'll have to pay $5")
else:
    print(f"Because you are {attendees}, you'll be required to pay $10")