# A function to check if a word is a palindrome
# By Ted Silbernagel

def checkPalindrome(inputWord):
  reversedWord = ''
  for letter in reversed(inputWord):
    reversedWord += letter
  if inputWord == reversedWord:
    print(f'Yes, {inputWord} is a palindrome.')
  else:
    print(f'No, {inputWord} is not a palindrome.')

# Ask user for a string to reverse
print('This program will check to see if a given word is a palindrome.')
stringToReverse = input('Please enter a word: ')

# Run function, print results
checkPalindrome(stringToReverse)