# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

# Places that I wish to visit
places = ['maldives', 'santorini', 'sierra leone', 'dubai', 'oslo']
print(f"{places}\n") # here the list is in its original order

# sort the places in alphabetical order temporarily
print(sorted(places))

print(f"\n{places}") # print the list in its original format back again

# print the list alphabetically in reverse order using sorted
print(f"\n{sorted(places, reverse = True)}")

print(f"\n{places}\n") # here the list is in its original order

# print broken lines for clearity
print("-" * 30)
# headline
print("List in reverse order")
# print broken lines for clearity
print("-" * 30)

# printing the list in reverse order
places.reverse()
print(f"{places}\n") # the list in reverse order

# printing the list in reverse order again
places.reverse()
print(f"{places}\n") # the list in reverse order


# print broken lines for clearity
print("-" * 30)
# headline
print("List sort alphabetically")
# print broken lines for clearity
print("-" * 30)

# using sort to change the order of the list alphabetically
places.sort()
print(f"{places}\n") # the list in reverse order

# using sort to change the order of the list in reverse alphabet 
places.sort(reverse=True)
print(f"{places}\n") # the list in reverse order