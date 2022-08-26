# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

# List of people I would invite to my graduation
invitees = ['Aunty Rassie', 'Aminata', 'Halley', 'Mary', 'Ibrahim', 'Freda']

# One of my invitees opt out
removed_invitee = invitees.pop(4)

# Invintee who cannot make my graduation
print(f"Unfortunately, {removed_invitee} can\'t make it to my graduation!\n")

# Replace the opt out invitee with another
new_invitee = invitees.insert(4, 'Aba Kamara')

# Invite message
invite_message = "I would like to invite you to my graduation!"

# Updated list of invitees
# send the invite message
print(f"Hi {invitees[0]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[1]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[2]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[3]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[4]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[5]}, {invite_message}\n")

# Print a line of seperation between old and updated invitees
print('-' * 65)

# Informing my current guest that there will be more guests
print("Hi current invitees, there will be more guest to my graduation!")

# Print a line of seperation between old and updated invitees
print('-' * 65)
print() # blank space

# Adding a guest in the beginning of my List
invitees.insert(0, 'Titus')

# Adding a guest at the middle of my List
invitees.insert(3, 'Abdul')

# Adding a guest at the end of my List
invitees.append('Rahman')

# Updated list of invitees
# send the invite message
print(f"Hi {invitees[0]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[1]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[2]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[3]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[4]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[5]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[6]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[7]}, {invite_message}\n")

# send the invite message
print(f"Hi {invitees[8]}, {invite_message}\n")

# Indicating the number of people I am inviting
print(f"I am inviting a total number of {len(invitees)} people to my graduation!")