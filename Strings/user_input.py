# Ask the user for their name
name = input("What is your name? ")
print(f"Welcome, {name.title()}!\n") # Welcome message with the input user name first letter in capital letter

# Ask the user for their age
age = int(input("How old are you? "))
# add one year to the age the use entered
print(f"Next year, {name.title()} would be {age + 1} years old!")