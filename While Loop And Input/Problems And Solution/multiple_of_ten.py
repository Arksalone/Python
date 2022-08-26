# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

# ask the user to enter a number
multiple_of_ten = int(input("Pleae enter a number! "))

# check if the number is multiple of 10
if multiple_of_ten % 10 == 0:
    print(f"\n{multiple_of_ten} is a multiple of ten.")
else:
    print(f"\n{multiple_of_ten} is not a multiple of ten.")