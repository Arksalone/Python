# This is list comprehension
# print numbers raised to the power of three from 0 to 20
numbers = [value ** 3 for value in range(0, 20)]
print(numbers)

my_name = [letters for letters in 'Abdulrahman']
print(my_name)

# calculating temperature using for loop
# store the temperature to be calculated in a variable
celcius = [12, 89, -23, 78, -65, -9]

fahrenheit = [] # empty list
for temp in celcius:
    temp_calculation = ((9 / 5) * temp + 32)
    fahrenheit.append(temp_calculation) 

print(fahrenheit)