# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
# chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

alien_color = 'green' # alien color

print("First Version")

# using an if statement to test if the color match
if alien_color == 'green':
    print("Congratulation, you just earned five points!")
elif alien_color == 'yellow':
    print("Congratulation, you just earned ten points!")
elif alien_color == 'red':
    print("Congratulation, you just earned fifteen points!")

print("\nSecond Version")

alien_color = 'yellow' # alien color

# using an if statement to test if the color match
if alien_color == 'green':
    print("Congratulation, you just earned five points!")
elif alien_color == 'yellow':
    print("Congratulation, you just earned ten points!")
elif alien_color == 'red':
    print("Congratulation, you just earned fifteen points!")


print("\nThird Version")

alien_color = 'red' # alien color

# using an if statement to test if the color match
if alien_color == 'green':
    print("Congratulation, you just earned five points!")
elif alien_color == 'yellow':
    print("Congratulation, you just earned ten points!")
elif alien_color == 'red':
    print("Congratulation, you just earned fifteen points!")