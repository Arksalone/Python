# Consider a list of newly registered but unverified users of a website. After
# we verify these users, how can we move them to a separate list of confirmed
# users?

# Store the unverify user in a variable
unverified_users = ['abdul', 'rahman', 'kabia']

# Store verified user in an empty list
verified_users = []

while unverified_users:
    confirmed_users = unverified_users.pop() # remove unverified users and store them in confirmed users variable
    # print the confirmed users
    print(f"These are the confirmed users: {confirmed_users.title()}")

    verified_users.append(confirmed_users) # add all confirmed users to be verifoed

print() # this print a blank space

# print out all verified users through a for loop
print("These users have been verified:")
for verified_users in verified_users:
    print(verified_users.title())