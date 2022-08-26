# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
# store the numbers in an empty list
numbers = []

for number in range(0, 21): # iterating from range zero to twenty one
    numbers.append(number) # add number to the end so that it prints in a list format

print(numbers)