# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

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

# Print a line of seperation between old and updated invitees
print('-' * 70)

# Informing my current guest that there will be more guests
print("List needs to be reshuffle so that I can only invite two people, sorry!")

# Print a line of seperation between old and updated invitees
print('-' * 70)
print() # blank space

# Removing guest from list one at a time
# Removing first guest
first_guest = invitees.pop(0)
print(f"Hi {first_guest}, your invitation has been revoked!\n") # let this person know they are no longer invited

# Removing second guest
second_guest = invitees.pop(1)
print(f"Hi {second_guest}, your invitation has been revoked!\n") # let this person know they are no longer invited

# Removing third guest
third_guest = invitees.pop(2)
print(f"Hi {third_guest}, your invitation has been revoked!\n") # let this person know they are no longer invited

# Removing fourth guest
fourth_guest = invitees.pop(3)
print(f"Hi {fourth_guest}, your invitation has been revoked!\n") # let this person know they are no longer invited

# Removing fifth guest
fifth_guest = invitees.pop(4)
print(f"Hi {fifth_guest}, your invitation has been revoked!\n") # let this person know they are no longer invited

# Removing seventh guest
seventh_guest = invitees.pop(3)
print(f"Hi {seventh_guest}, your invitation has been revoked!\n") # let this person know they are no longer invited

# Removing eight guest
eight_guest = invitees.pop(2)
print(f"Hi {eight_guest}, your invitation has been revoked!\n") # let this person know they are no longer invited

# Print a line of seperation between old and updated invitees
print('-' * 70)

# Informing my current guest that there will be more guests
print("Letting the remaing invitees know they are still invited!")

# Print a line of seperation between old and updated invitees
print('-' * 70)
print() # blank space


# These are the only people in my list so far that will attend my graduation
print(f"Hi {invitees[0]} and {invitees[1]}, you both are still invited!\n")

# Print a line of seperation between old and updated invitees
print('-' * 50)

# Informing my current guest that there will be more guests
print("An empty list after everyone has been deleted!")

# Print a line of seperation between old and updated invitees
print('-' * 50)
print() # blank space

# Delete everyone from my invitation list
del invitees[0:2]

# Showcase my empty list after everyone has been deleted!
print(invitees)