# What is available at the restaurant
available_toppings = ['tomatoes', 'cucumber', 'avocado', 'sweet cream']

# toppings that I need
toppings_needed = ['avocado', 'tomatoes', 'cucumber', 'fish', 'sweet cream', 'beef']

# iterate through the available toppings with for loop
for toppings in toppings_needed:
    if toppings in available_toppings: # check if the toppings I need is available with the restaurant toppings
        print(f"Adding {toppings}.")
    else:
        print(f"We are currently out of {toppings}")