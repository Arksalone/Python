while True:
    print("Who are you? ")
    name = input()
    if name != 'Abdulrahman':
        continue
    print("What is the password? ")
    password = input()
    if password == 'pass':
        break
print("You are in!")