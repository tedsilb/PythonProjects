# A function to reverse a string
# By Ted Silbernagel


def reverseString(inputWord):
  wordToReverse = inputWord
  returnWord = ''
  for _ in wordToReverse:
    returnWord += wordToReverse[-1:]
    wordToReverse = wordToReverse[:-1]
  return returnWord

# Get user string, run function, print results
print(reverseString(input('Please enter a word/string to reverse: ')))
