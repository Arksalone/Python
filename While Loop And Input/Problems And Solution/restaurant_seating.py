# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

# Ask the user the anount of seat they want and stored in a variable
restaurant_seating = int(input("How many people are there in your dinner group? "))

# check if the amount of people needed in their group per dinner is more than eight
if restaurant_seating > 8:
    print("\nplease wait for the next available seating!")
else:
    print("\nWe have available seating, come on in!")