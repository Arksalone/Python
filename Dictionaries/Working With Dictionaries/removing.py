# removing or deleting from a dictionary
information = {'name': 'Abdulrahman', 'age': 12, 'city': 'herndon'}
print(f"Original information: \n{information}") # this prints the orignal information of the user

print() # this prints a blank line

# The age information is no longer needed and should be removed
del information['age']
print(f"Information after age has been removed: \n{information}") # this prints after age has been deleted