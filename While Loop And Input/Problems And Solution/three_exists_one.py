# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.

# Ask the user to enter pizza toppings
prompt = "\nPlease enter your favorite pizza toppings: \nType 'quit' to exit! "

while True:
    message = input(prompt)
    if message.lower() == 'quit':
        print("\nDone!")
        break

    else:
        print(f"\nI like {message} toppings also.")