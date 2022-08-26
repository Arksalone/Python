# information on different types of cars
cars = {
    'make': 'toyota',
    'model': ['corolla', 'camry'],
    }

# make a summary of cars that you have
print(f"You have {cars['make'].title()} with the following model: ")

# print the list of model
for different_model in cars['model']:
    print(f"{different_model.title()}")