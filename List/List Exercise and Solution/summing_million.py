# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

# list of numbers from one to one million
numbers = []

# using a for loop to print one to one million
for number in range(1, 1_000_001):
    numbers.append(number) # add number into numbers

print(f"{numbers}") # print all numbers from one to one million
print() # blank space
print(f"The maximum number is {max(numbers)}.\n") # prints the maximum number
print(f"The minimum number is {min(numbers)}.\n") # prints the minimum number
print(f"The sum of all the numbers are {sum(numbers)}.\n") # prints the sum of all numbers