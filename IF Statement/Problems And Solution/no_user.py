# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.

# empty admin list
admins = []

if admins: # check if the list is empty
    # use for loop to iterate through the empty list
    for admin in admins:
        print(f"Hello {admin.title()}, would you like to see a status report?") # print this if list not empty
else:
    print("We need to find some users!") # print this if list is empty
