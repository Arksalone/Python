# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_number = {
    'abdul': [2, 5, 7, 8],
    'rahman': [10, 8, 56, 3],
    'kabia': [9, 0, 6, 67],
    'ark': [4, 40, 44, 35],
    'arksalone': [77, 16, 17, 20],
}

for names, favorite_digits in favorite_number.items(): # this loop through the list in the dictionary
    print(f"\n{names.title()} favorite numbers are:") # prints the name of people
    for numbers in favorite_digits: # loop through the numbers
        print(numbers)