# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubic_numbers = [] # store the numbers in an empty list

for cubic in range(1, 11):
    cube_calc = cubic ** 3 # store the cube calculation in a variable
    cubic_numbers.append(cube_calc) # add the calculation inside the empty list

print(cubic_numbers)