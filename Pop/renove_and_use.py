# List of items
item = [1, "Abdul", "Rahman", "Kabia"]

# print the items
print(item)

# remove one item
item_removed = item.pop()
print() # blank space

# print the list after an item has been removed
print(item)
print() # blank space

# print the item that was removed
print(f"\tMy last name \"{item_removed}\" was removed \nthe list!")
print() # blank space

# Removing my middle name from the list
middle_name = item.pop(2)

# print a statement showing that my middle name was removed
print(f"\tMy name would have been shorter if was not \nfor my middle name \"{middle_name}\".")
print() # blank space

# Debugging to see what is slowing down my atom
print("I am trying to see what is slowing down my atom! \nI found out that it was the package \"pigment\"!")