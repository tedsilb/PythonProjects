# This program will encrypt and decrypt messages using a Vigenere cipher
# By Ted Silbernagel

# Import dependencies
import string
from copy import deepcopy


# Define function to shift list a certain number of times
def shiftList(listToShift, numberToShift, direction):
  newList = deepcopy(listToShift)
  for _ in range(0, numberToShift):
    if direction == 'forward':
      # Insert the first item at the end of the list
      firstItem = newList[0]
      newList.append(firstItem)
      # Remove the first item
      newList.pop(0)
    elif direction == 'back':
      # Insert the last item at the start of the list
      lastItem = newList[-1]
      newList.insert(0, lastItem)
      # Remove the last item
      newList.pop()
  return newList


# Define function to fill key to specified length
def fillKey(key, length):
  newKey = key
  while len(newKey) < length:
    if (length - len(newKey)) >= len(key):
      newKey += key
    else:
      numberToSlice = int(float(length) % float(len(newKey)))
      newKey += key[:numberToSlice]
  return newKey


# Define function to translate data
def vigCrypt(rawString, userKey, cryptBase, operation):
  # Set up string to store translated message
  translatedMsg = ''

  # Set up dict to determine shift direction
  shiftDirs = {
    'Encrypt': 'forward',
    'Decrypt': 'back',
  }

  # Run through string, translate message
  n = 0
  for letter in rawString:
    # Find position of letter in cryptBase
    letterPos = cryptBase.index(letter)

    # Find position of key letter in cryptBase
    keyLetterPos = cryptBase.index(userKey[n])

    # Create shifted cryptBase for this letter
    shiftedCryptBase = shiftList(cryptBase, keyLetterPos, shiftDirs[operation])

    # Get the translated letter, add to translated message
    translatedMsg += shiftedCryptBase[letterPos]

    # Increment n counter
    n += 1

  # Return decrypted string
  return f'{operation}ed message: {translatedMsg}'


# Define main function
def vigenere():
  # Ask user to encrypt/decrypt
  operation = input('Would you like to (e)ncrypt or (d)ecrypt? ').lower()

  # Gather string from user
  if operation in ['encrypt', 'e']:
    operation = 'Encrypt'
    stringCrypt = input('Please enter a message to encrypt (no numbers): ')
  elif operation in ['decrypt', 'd']:
    operation = 'Decrypt'
    stringCrypt = input('Please enter a message to decrypt: ')
  else:
    print('Please enter a valid operation.')
    quit()

  # Uppercase string and remove spaces
  stringCrypt = stringCrypt.upper().replace(" ", "")

  # Make translator objects to strip puncuation and digits
  remove_punctuation = str.maketrans('', '', string.punctuation)
  remove_digits = str.maketrans('', '', string.digits)

  # Strip punctuation and digits from string
  stringCrypt = stringCrypt.translate(remove_punctuation).translate(remove_digits)

  # Ask user for key, make uppercase and remove spaces
  key = input('Please enter your key (a word): ').upper().replace(" ", "")

  # Repeat the key to match the length of the string
  key = fillKey(key, len(stringCrypt))

  # Set up list of letters to use in crypto operations
  cryptBase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  # Run translation
  return vigCrypt(stringCrypt, key, cryptBase, operation)


# Call main function, print returned data
print(vigenere())
