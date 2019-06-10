# This program will encrypt and decrypt messages using a Caesar cipher
# By Ted Silbernagel

# Import dependencies
import string

# Define function to encrypt and decrypt
def caesarCipher():
  # Define encrypt function
  def cEncrypt(listToEncrypt, encryptionKey):
    # Set up list to store encrypted words
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

  # Define decrypt function
  def cDecrypt(listToDecrypt, decryptionKey):
    # Set up list to store decrypted words
    decryptedList = []

    # Run thorough list, decrypt words
    for word in listToDecrypt:
      currentWord = ''
      for letter in word:
        currentIndex = cryptBase.index(letter) + 1
        newIndex = (currentIndex - decryptionKey + 26) % 26
        newIndex -= 1
        currentWord += cryptBase[newIndex]
      decryptedList.append(currentWord)

    # Rejoin list to string
    encryptedString = ' '.join(decryptedList)

    # Return string
    return encryptedString

  # Set up list of alphabet to use for encryption/decryption
  cryptBase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
  cryptBase += ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  # Ask user to encrypt/decrypt
  operation = input('Would you like to (e)ncrypt or (d)ecrypt? ').lower()

  # Gather string from user
  if operation == 'encrypt' or operation == 'e':
    operation = 'e'
    stringCrypt = input('Please enter the word or string to encrypt: ')
  elif operation == 'decrypt' or operation == 'd':
    operation = 'd'
    stringCrypt = input('Please enter the word or string to decrypt: ')

  # Make translator object to strip puncuation
  translator = str.maketrans('', '', string.punctuation)

  # Strip punctuation from string
  stringCrypt = stringCrypt.translate(translator)

  # Uppercase the entire string
  stringCrypt = stringCrypt.upper()

  # Split string into list
  listCrypt = stringCrypt.split(' ')

  # Ask user for key
  key = int(input('Please enter the key to use (1 to 25): '))

  # Run encrypt or decrypt function, catch response
  if operation == 'e':
    response = cEncrypt(listCrypt, key)
  elif operation == 'd':
    response = cDecrypt(listCrypt, key)

  # Return response
  return response

# Call function, print response
response = caesarCipher()
print(response)
