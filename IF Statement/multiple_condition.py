user = ['abdul', 'rahman', 'kabia', 'aminata'] # list of names that are allowed entry

banned_user = 'halley' # this user is not allowed entry

# check if a user is in the list
invited_user = 'abdul'

# Check if banned user is in the list
if banned_user not in user:
    print(f"Sorry {banned_user.title()}, you are not allowed to enter!")

print() # print blank space

# check if invited user is allowed to enter
if invited_user in user:
    print(f"Welcome {invited_user.title()}, you are allowed to enter!")