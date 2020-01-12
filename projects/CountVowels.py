# This program will count the number of vowels in a string
# By Ted Silbernagel

from typing import Text


def count_vowels(input_string: Text):
  # Set up count vars for vowels
  counts = {
    'A': 0,
    'E': 0,
    'I': 0,
    'O': 0,
    'U': 0,
  }

  # Start looping through the string
  for char in input_string.upper():
    if char in counts.keys():
      counts[char] += 1

  # Print counts for user
  for vowel, count in counts.items():
    if count:
      print(f'{vowel}: {count}')

# Call function
print('This program will count the number of vowels in a word/string.')
user_string = input('Please enter a string: ')
count_vowels(user_string)
