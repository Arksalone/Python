# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

# programming words I have learned and their meaning
programming_words = {
    'break': 'means to exit a loop',
    'continue': 'means to skip a character',
    'iteration': 'means to go through',
    'dictionary': 'means the collection of key value pairs',
    'tuples': 'is similar to list but are immutable',
    'set': 'filter repetitive words',
    'strip': 'removes blank spaces',
    'len': 'count lenght of word',
    }

for words, meaning in programming_words.items():
    print(f"{words.title()}: This {meaning}.")
