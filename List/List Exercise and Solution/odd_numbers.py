# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.

# store the numbers in a list
odd_numbers = []

for number in range(1, 21, 2): # this prints only odd numbers
    odd_numbers.append(number)

print(odd_numbers) # prints the numbers