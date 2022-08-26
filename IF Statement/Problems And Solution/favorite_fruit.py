# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!

# list of my favorite fruits
favorite_fruits = ['banana', 'avocado', 'orange', 'apple']

# check if certain fruit is available in my list
if 'banana' in favorite_fruits:
    print("You have banana in the list!\n")
if 'pineapple' not in favorite_fruits:
    print("You do not have pineapple in the list!\n")
if 'avocado' in favorite_fruits:
    print("You have avocado in the list!\n")
if 'apple' in favorite_fruits:
    print("You have apple in the list!\n")
if 'orange' in favorite_fruits:
    print("You do not eat orange often!\n")