"""This program will encrypt and decrypt messages using a Caesar cipher.
By Ted Silbernagel
"""

import string
from typing import List


def caesar_encrypt(list_to_encrypt: List[str], encryption_key: int,
                   crypt_base: List[str]) -> str:
  # List to store encrypted words
  encrypted_list = []

  # Run thorough list, encrypt words
  for word in list_to_encrypt:
    current_word = ''
    for letter in word:
      current_index = crypt_base.index(letter) + 1
      new_index = (current_index + encryption_key) % 26
      new_index -= 1
      current_word += crypt_base[new_index]
    encrypted_list.append(current_word)

  # Rejoin list to string
  encrypted_string = ' '.join(encrypted_list)

  return encrypted_string


def caesar_decrypt(list_to_decrypt: List[str], decryption_key: int,
                   crypt_base: List[str]) -> str:
  # List to store decrypted words
  decrypted_list = []

  # Run through list, decrypt words
  for word in list_to_decrypt:
    current_word = ''
    for letter in word:
      current_index = crypt_base.index(letter) + 1
      new_index = (current_index - decryption_key + 26) % 26
      new_index -= 1
      current_word += crypt_base[new_index]
    decrypted_list.append(current_word)

  # Rejoin list to string
  decrypted_string = ' '.join(decrypted_list)

  return decrypted_string


def caesar_crack(list_to_crack: List[str], crypt_base: List[str]) -> str:
  print('Crack starting. Press enter to try again or any other key to exit.')

  # Try each combination
  for i in range(1, 27):
    # Set up list to store cracked words
    cracked_list = []

    # Run thorough list, crack words
    for word in list_to_crack:
      current_word = ''
      for letter in word:
        current_index = crypt_base.index(letter) + 1
        new_index = (current_index - i + 26) % 26
        new_index -= 1
        current_word += crypt_base[new_index]
      cracked_list.append(current_word)

    # Rejoin list to string
    cracked_string = ' '.join(cracked_list)

    # Ask user if this makes sense or to try again
    if (input(f'Attempt {i}/26: "{cracked_string}": Correct? ').lower()
        not in ['', 'n']):
      return cracked_string

  # Otherwise, let the user know crack was unsuccessful
  return 'Crack unsuccessful.'


def caesar_cipher() -> str:
  # Set up list of alphabet to use for encryption/decryption
  crypt_base = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  # Ask user to encrypt/decrypt
  operation = input('Would you like to (e)ncrypt, (d)ecrypt, or (c)rack? '
                   ).lower()

  # Gather string from user
  if operation in ['encrypt', 'e']:
    operation = 'e'
    string_crypt = input('Please enter the message to encrypt: ')
  elif operation in ['decrypt', 'd']:
    operation = 'd'
    string_crypt = input('Please enter the message to decrypt: ')
  elif operation in ['crack', 'c']:
    operation = 'c'
    string_crypt = input('Please enter the message to crack: ')
  else:
    raise Exception(f'Invalid operation entered: {operation}')

  # Make translator object to strip punctuation
  translator = str.maketrans('', '', string.punctuation)

  # Strip punctuation, uppercase, split into list
  list_crypt = string_crypt.translate(translator).upper().split(' ')

  # If not cracking, ask user for key
  if operation != 'c':
    key = int(input('Please enter the key to use (1 to 25): '))

  # Run encrypt or decrypt function, return response
  if operation == 'e':
    return caesar_encrypt(list_crypt, key, crypt_base)
  elif operation == 'd':
    return caesar_decrypt(list_crypt, key, crypt_base)
  elif operation == 'c':
    return caesar_crack(list_crypt, crypt_base)


# Call function, print response
print(caesar_cipher())
