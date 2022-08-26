# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

# my favorite restaurant
favorite_food = ('cava', 'mezeh mediterranian', 'sweet greans', 'chipotle')

# headline message
print("My favorite restaurants are:")
# print out the restaurant using for loop
for restaurant in favorite_food:
    print(f"{restaurant.title()}")

# print a blank space between the two list
print()

# redefining my favorite food
favorite_food = ('wendys', 'mezeh mediterranian', 'cold stone creamy', 'chipotle')
# headline message
print("My updated favorite restaurants are:")
# print out the restaurant using for loop
for restaurant in favorite_food:
    print(f"{restaurant.title()}")

