# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

# dictionary containing three major rivers
major_rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'amazon': 'peru',
    }

# A sentence about each rivers
for river, region in major_rivers.items():
    print(f"River {river.title()} runs through {region.title()}.")