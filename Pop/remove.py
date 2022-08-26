# Work with item that is being removed from list
item = ['Abdul', 'Rahman', 'Kabia', 'Ark', 'Arkslus']
print(item)
print() # blank space

removed_item = item.pop(3)
print(removed_item) # item that was removed
print() # blank space

# deleting an item
del item[2]
print(item)
print() # blank space

# Removing an item
item.remove("Arkslus")
print(item)