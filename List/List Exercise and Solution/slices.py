# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.

my_family = ['ramatu', 'yealie', 'alimatu', 'aminata', 'yusif']

# message to the list
print("The first three items in the list are:")
# loop through the list to find the first three items
for name in my_family[0:3]:
    print(f"{name.title()}")

# message to the list
print("\nThree items from the middle of list are:")
# find three items from the middle
for name in my_family[1:4]:
    print(f"{name.title()}")

# message to the list
print("\nThe last three items from the list are:")
# finding the last three items from the list
for name in my_family[2:]:
    print(f"{name.title()}")



