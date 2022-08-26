# Statement
print("This prints the numbers on each line!")
# print number 1 through 10
for value in range(1, 11):
    print(f"{value}")

print() # line space

# odd numbers
even_numbers = list(range(2, 20, 2))
print(min(even_numbers))
print(f"This prints even numbers:\n{even_numbers}\n")

# Statement
print("This prints the numbers in a list!")
# Place the numbers in a list
numbers = []
# print number 1 through 10
for value in range(1, 11):
    numbers.append(value)

print(sum(numbers))
print(f"{numbers}\n") # print the numbers

# Statement
print("This program prints the  square of numbers in a list from 1 through 10!")
# This program prints the sqaures of numbers from 1 to 30
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
print(max(squares))