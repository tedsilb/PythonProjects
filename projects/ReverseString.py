# A function to reverse a string

def reverseString(inputWord):
  returnWord = ''
  for letter in reversed(inputWord):
    returnWord += letter
  return returnWord

# Ask user for a string to reverse
stringToReverse = input('Please enter a word/string to reverse: ')

# Run function, print results
response = reverseString(stringToReverse)
print(response)