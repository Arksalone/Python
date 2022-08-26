# my friends and their favorite language
favorite_language = {
    'abdul': 'python',
    'rahman': 'sql',
    'kabia': 'excel',
    'ark': 'javascript',
    'aminata': 'excel',
    }

# get all values without repetition
print("These are my favorite languages:")
for language in set(favorite_language.values()):
    print(f"{language.title()}.")