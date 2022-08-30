# using break to exit the loop

# Ask the user to enter cities they have been to and type quit to exit
prompt = "\nPlease enter the cities you have been to: \nType 'quit' when done! "

while True:
    city = input(prompt) # print to the screen whatever the user entered

    if city.lower() == 'quit': # if user enter 'quit' exit the loop
        break
    else:
        print(f"\n{city.title()} is a beautiful city!") # print the city entered by the user with a message