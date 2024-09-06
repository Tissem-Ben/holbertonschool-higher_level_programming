#!/usr/bin/python3

word = "Holberton"

word_first_3 = word[:3]       # Contains the first 3 letters of `word`
word_last_2 = word[-2:]       # Contains the last 2 letters of `word`
middle_word = word[1:-1]      # Contains `word` without the first and last letters

print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
