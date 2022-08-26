# Alien information
alien = {'first_postition': 2, 'second_position': 3, 'speed': 'medium'}
print(f"This is the original alien position: {alien['first_postition']}.") # print the first original alien position

print() # print a blank line

# increase the alien position with respect to its speed
if alien['speed'] == 'fast':
    increase_speed = 5
elif alien['speed'] == 'medium':
    increase_speed = 4
else:
    increase_speed == 1

# increment the speed of the alien
alien['first_postition'] += increase_speed
# print the final position of the alien
print(f"This is the final position of the alien: {alien['first_postition']}.")
