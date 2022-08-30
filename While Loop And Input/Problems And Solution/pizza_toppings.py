# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

# ask the user to enter pizza toppings they like
prompt = "\nPlease enter pizza toppings that you like: \nType quit when done! "

# stored user input in an empty string
message = " "

while message.lower() != 'quit': # check if the message enter by the user is not equals 'quit'
    message = input(prompt)

    if message != 'quit':
        print(f"\n{message.title()} is a good choice of topping!")