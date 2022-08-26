# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

# dictionary containing cities
cities = {
    'freetown': {
        'country': 'sierra leone',
        'population': 500,
        'fact': 'home to beautiful sea beaches',
    },

    'sterling': {
        'country': 'United States',
        'population': 1000,
        'fact': 'close to the capital',
    },

    'lome': {
        'country': 'togo',
        'population': 700,
        'fact': 'one of the smallest city in Africa',
    }
}

# loop through the cities to print information about each cities
for city, information in cities.items():
    print(f"\n Name of city: {city.title()}.")
    print(f"\tCountry: {information['country'].title()}.")
    print(f"\tPopulation: {information['population']}.")
    print(f"\tFact: {information['fact'].title()}.")