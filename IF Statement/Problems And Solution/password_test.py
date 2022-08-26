# Store the password in a variable
password = 'Alhamdulilah'

# Ask user to enter their password
user_input = input('Please enter your password! ')
# Use if statement for test cases
if user_input == password:
    print(f"Yes, the password is {password}!")
else:
    print("Sorry, that password is incorrect!")