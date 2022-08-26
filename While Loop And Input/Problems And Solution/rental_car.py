# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

# Ask the user the type of car they want to rent
rental_car = str(input("What kind of car do you wish to rent? "))

# print a check message if the rental car carries the particular car the user asked for
print(f"\nLet us see if we can find you {rental_car.title()}.")