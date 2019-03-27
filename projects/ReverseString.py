# A function to reverse a string
# By Ted Silbernagel

def reverseString(inputWord):
  wordToReverse = inputWord
  returnWord = ''
  for _ in wordToReverse:
    returnWord += wordToReverse[-1:]
    wordToReverse = wordToReverse[:-1]
  return returnWord

# Ask user for a string to reverse
stringToReverse = input('Please enter a word/string to reverse: ')

# Run function, print results
response = reverseString(stringToReverse)
print(response)
