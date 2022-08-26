# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.

# my original pizza places
my_pizza = ["papa john's", "paissano", "cheestique", "jimmy john's"]

# print my pizza places
print(f"These are my original pizza places: \n{my_pizza}")

# my friends pizza places
my_friend_pizza = my_pizza[::]
# print my friend's pizza places
print(f"\nThese are my friend's pizza places: \n{my_friend_pizza}")

# adding a new place to the original list
my_pizza.append("Little Ceasar")
print(f"\nAn item added to my original pizza places: \n{my_pizza}")

# adding a new place to my friend pizza places
my_pizza.append("dmv pizza")
print(f"\nAn item added to my friend's pizza places: \n{my_friend_pizza}")