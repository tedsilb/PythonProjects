# A function to check if a word is a palindrome
# By Ted Silbernagel

from typing import Text


def is_palindrome(input_word: Text) -> bool:
  if input_word == input_word[::-1]:
    return True
  else:
    return False

# Ask user for a string to reverse
print('This program will check to see if a given word is a palindrome.')
string_to_check = input('Please enter a word: ')

# Call function, print results
if is_palindrome(string_to_check):
  print(f'Yes, {string_to_check} is a palindrome.')
else:
  print(f'No, {string_to_check} is not a palindrome.')
