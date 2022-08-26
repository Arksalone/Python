# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.

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