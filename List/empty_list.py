# empty list
names = []

# Adding values to the list
names.append("Abdul")
names.append("Rahman")
names.append("Kabia")
names.append("The Software Developer")

# insert values into the list
names.insert(3, "Ark")
names.insert(5, "InshaaAllah")
names.insert(6, "This should be removed!")

#print the list
print(names)

# deleting an item from the list
del names[6]

# print the final list after deletion of a value
print(f"\n{names}")