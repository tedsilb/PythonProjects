# This program will encrypt and decrypt messages using a Vigenere cypher
# By Ted Silbernagel

# Import dependencies
import string
from copy import deepcopy

# Define main function
def vigenere():
  # Define function to shift list a certain number of times
  def shiftList(listToShift, numberToShift):
    newList = deepcopy(listToShift)
    print(listToShift)
    print(newList)
    for _ in range(0, numberToShift):
      # Insert the first item at the end of the list
      firstItem = newList[0]
      newList.append(firstItem)
      # Remove the first item
      newList.pop(0)
    print(f'Shifting {listToShift} by {numberToShift} to {newList}')
    return newList

  # Define function to encrypt data
  def vigEncrypt(stringToEncrypt, userKey):
    # Set up string to store encrypted message
    encryptedMsg = ''

    # Run through string, encrypt message
    n = 0
    for letter in stringToEncrypt:
      # Find position of letter in cryptBase
      letterPos = cryptBase.index(letter)

      # Find position of key letter in cryptBase
      keyLetterPos = cryptBase.index(userKey[n])

      # Create shifted cryptBase for this letter
      shiftedCryptBase = shiftList(cryptBase, keyLetterPos)

      # Get the encrypted letter
      encryptedLetter = shiftedCryptBase[letterPos]

      # Add encrypted letter to encrypted message
      encryptedMsg += encryptedLetter

      # Increment n counter
      n += 1

    # Return string
    return encryptedMsg

  # Define function to decrypt data
  def vigDecrypt(stringToDecrypt, userKey):
    return 'temp'

  # Ask user to encrypt/decrypt
  operation = input('Would you like to (e)ncrypt or (d)ecrypt? ').lower()

  # Gather string from user
  if operation == 'encrypt' or operation == 'e':
    operation = 'e'
    stringCrypt = input('Please enter a message to encrypt (no numbers): ')
  elif operation == 'decrypt' or operation == 'd':
    operation = 'd'
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
  stringCrypt = stringCrypt.translate(remove_punctuation)
  stringCrypt = stringCrypt.translate(remove_digits)

  # Ask user for key
  key = input('Please enter your key (a word): ').upper().replace(" ", "")

  # Repeat the key to match the length of the string
  newKey = key
  while len(newKey) < len(stringCrypt):
    if (len(stringCrypt) - len(newKey)) >= len(key):
      newKey += key
    else:
      numberToSlice = int(float(len(stringCrypt)) % float(len(newKey)))
      newKey += key[:numberToSlice]
  key = newKey

  # Set up list of letters to use in crypto operations
  cryptBase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
  cryptBase += ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  print(cryptBase)

  # Call function based on user input
  if operation == 'e':
    result = vigEncrypt(stringCrypt, key)
    return result
  elif operation == 'd':
    result = vigDecrypt(stringCrypt, key)
    return result
  else:
    print('Please enter a valid operation.')
    quit()

# Call function, print returned data
response = vigenere()
print(response)
