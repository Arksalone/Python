# Ask the user to type anything until the user enter "quit" to stop the program
prompt = "\nTell me anything and I will return it back to you. \nType 'quit' to end the program: "
# prompt += "\nType 'quit' to end the program! "

message = " " # stored what the user entered in an empty string

while message.lower() != 'quit': # convert quit to lowercase if the user enter quit
    message = input(prompt)

    if message != 'quit':
        print(f"\n{message}")  # print whatever the user entered