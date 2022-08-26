# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

# programming words I have learned and their meaning
programming_words = {
    'break': 'means to exit a loop',
    'continue': 'means to skip a character',
    'iteration': 'means to go through',
    'dictionary': 'means the collection of key value pairs',
    'tuples': 'is similar to list but are immutable',
    }

# loop through the glossary to print each word and its meaning
for word, meaning in programming_words.items():
    print(f"{word.title()}: this {meaning}.")