# printing only odd numbers using while loop and skip the even numbers

number = 0 # set number at zero

while number < 10:
    # increment the numbers by one
    number += 1
    if number % 2 == 0: # check for even numbers and skip
        continue
    else:
        print(number)