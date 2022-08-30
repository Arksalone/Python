# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

# Ask the user to enter their age
age = int(input("Please enter your age: "))

# set the range of age three
while age < 3: # check if the user age is under 3
    print(f"Since you are {age}, entry is free!")
    break

if age >= 3 and age <= 12: # check if the user age is between 3 and 12
    print(f"Since you are {age}, entry is $10.")
    
# And if the age over 12 do this:
else:
    print(f"Since you are {age}, entry is $12.")