# This program will count the number of vowels in a string
# By Ted Silbernagel

def countVowels(inputString):
  # Set up count vars for vowels
  countA = 0
  countE = 0
  countI = 0
  countO = 0
  countU = 0

  # Start looping through the string
  for char in inputString:
    if char.upper() == 'A':
      countA += 1
    elif char.upper() == 'E':
      countE += 1
    elif char.upper() == 'I':
      countI += 1
    elif char.upper() == 'O':
      countO += 1
    elif char.upper() == 'U':
      countU += 1

  # Return counts to user
  if countA != 0:
    print(f'A: {countA}')
  if countE != 0:
    print(f'E: {countE}')
  if countI != 0:
    print(f'I: {countI}')
  if countO != 0:
    print(f'O: {countO}')
  if countU != 0:
    print(f'U: {countU}')

# Call function
print('This program will count the number of vowels in a word/string.')
userString = input('Please enter a string: ')
countVowels(userString)
