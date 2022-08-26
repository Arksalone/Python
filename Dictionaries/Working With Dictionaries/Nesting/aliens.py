# create an empty dictionary to store aliens
aliens = []

# create 40 aliens using for loop and range
for alien_amount in range(0, 40):
    alien_created = {'color': 'green', 'points': 3, 'speed': 'slow'}
    aliens.append(alien_created)

# Print the first five aliens
for alien in aliens[:5]:
    print(f"{alien}")

print() # print a blank space

# change the characteristic or aliens starting 5 and end in 10
for alien in aliens[5:11]:
    if alien['color'] == 'green':
        alien['color'] = 'blue'
        alien['points'] = 10
        alien['speed'] = 'medium'

# Print alien from five to ten
for alien in aliens[5:11]:
    print(f"{alien}")

print() # print a blank space
# count the number of alien
print(f"The number of aliens are: {len(aliens)}.")