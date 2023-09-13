# But what if you want to remove all instances of a value
# from a list?
# Say you have a list of pets with the value 'cat' repeated several times.

# list all animals
animal = ['lion', 'tiger', 'cheetah', 'LiOn', 'dog', 'cat', 'LION']

# this is the original list
print(f"Original list: \n{animal}")

print() # blank space

# convert the list to lowercase
lower_animal = [animals.lower() for animals in animal]

# using while loop to remove duplicate animal
while 'lion' in lower_animal: # check for lion in the list
    lower_animal.remove('lion') # remove lion in the list

print(f"Edited list: \n{lower_animal}") # print the list after "lion" has been removed