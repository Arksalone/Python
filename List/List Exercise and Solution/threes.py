# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

numbers = []

for number in range(0, 31, 3): # looping to get multiples of threes
    numbers.append(number)

print(numbers)