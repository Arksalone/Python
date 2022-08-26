# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

# list of numbers from one to one million
numbers = []

# using a for loop to print one to one million
for number in range(1, 1_000_001):
    numbers.append(number)

print(numbers)