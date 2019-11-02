# A function to reverse a string
# By Ted Silbernagel


def reverseString(inputWord):
  returnWord = ''
  for _ in inputWord:
    returnWord += inputWord[-1:]
    inputWord = inputWord[:-1]
  return returnWord

# Get user string, run function, print results
print(reverseString(input('Please enter a word/string to reverse: ')))
