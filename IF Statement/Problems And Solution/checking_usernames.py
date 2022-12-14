# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.

# list of users
current_users = ['abdul', 'rahman', 'kabia', 'Ark', 'arkslus', 'arksalone']

# new users list
new_users = ['aRk', 'arksLUS', 'aminata', 'halley', 'mary']

# convert current users to lower case
lower_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f"{new_user} will need to enter a new user name!")
    else:
        print(f"{new_user} is available")