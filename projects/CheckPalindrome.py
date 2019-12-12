# A function to check if a word is a palindrome
# By Ted Silbernagel

from typing import Text


def isPalindrome(inputWord: Text) -> bool:
  if inputWord == inputWord[::-1]:
    return True
  else:
    return False

# Ask user for a string to reverse
print('This program will check to see if a given word is a palindrome.')
stringToCheck = input('Please enter a word: ')

# Call function, print results
if isPalindrome(stringToCheck):
  print(f'Yes, {stringToCheck} is a palindrome.')
else:
  print(f'No, {stringToCheck} is not a palindrome.')
