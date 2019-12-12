# This program will encrypt and decrypt messages using a Caesar cipher
# By Ted Silbernagel

import string
from typing import List, Text


def cEncrypt(listToEncrypt: List[Text], encryptionKey: Text,
             cryptBase: List[Text]) -> Text:
  # List to store encrypted words
  encryptedList = []

  # Run thorough list, encrypt words
  for word in listToEncrypt:
    currentWord = ''
    for letter in word:
      currentIndex = cryptBase.index(letter) + 1
      newIndex = (currentIndex + encryptionKey) % 26
      newIndex -= 1
      currentWord += cryptBase[newIndex]
    encryptedList.append(currentWord)

  # Rejoin list to string
  encryptedString = ' '.join(encryptedList)

  # Return string
  return encryptedString


def cDecrypt(listToDecrypt: List[Text], decryptionKey: Text,
             cryptBase: List[Text]) -> Text:
  # List to store decrypted words
  decryptedList = []

  # Run through list, decrypt words
  for word in listToDecrypt:
    currentWord = ''
    for letter in word:
      currentIndex = cryptBase.index(letter) + 1
      newIndex = (currentIndex - decryptionKey + 26) % 26
      newIndex -= 1
      currentWord += cryptBase[newIndex]
    decryptedList.append(currentWord)

  # Rejoin list to string
  decryptedString = ' '.join(decryptedList)

  # Return string
  return decryptedString


def cCrack(listToCrack: List[Text], cryptBase: List[Text]) -> Text:
  print('Crack starting. Press enter to try again or any other key to exit.')

  # Try each combination
  for i in range(1, 27):
    # Set up list to store cracked words
    crackedList = []

    # Run thorough list, crack words
    for word in listToCrack:
      currentWord = ''
      for letter in word:
        currentIndex = cryptBase.index(letter) + 1
        newIndex = (currentIndex - i + 26) % 26
        newIndex -= 1
        currentWord += cryptBase[newIndex]
      crackedList.append(currentWord)

    # Rejoin list to string
    crackedString = ' '.join(crackedList)

    # Ask user if this makes sense or to try again
    if (input(f'Attempt {i}/26: "{crackedString}": Correct? ').lower()
        not in ['', 'n']):
      return crackedString

  # Otherwise, let the user know crack was unsuccessful
  return 'Crack unsuccessful.'


def caesarCipher() -> Text:
  # Set up list of alphabet to use for encryption/decryption
  cryptBase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  # Ask user to encrypt/decrypt
  operation = input('Would you like to (e)ncrypt, (d)ecrypt, or (c)rack? '
                   ).lower()

  # Gather string from user
  if operation in ['encrypt', 'e']:
    operation = 'e'
    stringCrypt = input('Please enter the message to encrypt: ')
  elif operation in ['decrypt', 'd']:
    operation = 'd'
    stringCrypt = input('Please enter the message to decrypt: ')
  elif operation in ['crack', 'c']:
    operation = 'c'
    stringCrypt = input('Please enter the message to crack: ')
  else:
    print('Please enter a valid operation.')
    quit()

  # Make translator object to strip puncuation
  translator = str.maketrans('', '', string.punctuation)

  # Strip punctuation, uppercase, split into list
  listCrypt = stringCrypt.translate(translator).upper().split(' ')

  # If not cracking, ask user for key
  if operation != 'c':
    key = int(input('Please enter the key to use (1 to 25): '))

  # Run encrypt or decrypt function, return response
  if operation == 'e':
    return cEncrypt(listCrypt, key, cryptBase)
  elif operation == 'd':
    return cDecrypt(listCrypt, key, cryptBase)
  elif operation == 'c':
    return cCrack(listCrypt, cryptBase)

# Call function, print response
print(caesarCipher())
