# This madlib gives information about the user
# Ask the use for their name
name = str(input("What is your name? "))

# Ask the user for their favorite sport
sport = str(input("What is your favorite sport? "))

# Ask the user for their favorite food
food = str(input("What is your favorite food? "))

# print 80 lines
print("-" * 80)

# print the information about the user
print(f"Hi {name.title()}, it was nice meeting you! \n{sport.title()} is one of the most watched game in the world, \nand most loved as well. \nWe wish we could try {food} sometimes so that we know how it tastes! \nHurray to our new {food} dish!")

# print 80lines
print("-" * 80)