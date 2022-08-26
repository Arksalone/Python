# check for even and odd numbers by asking the user input
num = int(input("Enter a number to know if the number is even or odd! "))

# check if the number is divisible by two using modulo through an if else statement
if num % 2 == 0:
    print(f"\n{num} is an even number!")
else:
    print(f"\n{num} is an odd number!")