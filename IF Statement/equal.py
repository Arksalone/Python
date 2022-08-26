# list of my cars
my_cars = ['bmw', 'mercedes benz', 'volks wagen', 'audi', 'infinity']

# loop through my cars
for cars in my_cars:
    if cars == 'volks wagen': # check if this match one of my cars in the list
        print(cars.upper())
    else:
        print(cars.title())

# name of car written in different letter case
car = 'AuDi'

print() # print blank space
if car.lower() == 'audi': # using lower to bypass the case sensitive in the loop
    print("This is correct!")

print(car) # the value of car remains the same

