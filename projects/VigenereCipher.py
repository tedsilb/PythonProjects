# This program will encrypt and decrypt messages using a Vigenere cipher
# By Ted Silbernagel

import string
import copy
from typing import List


# Shift list a certain number of times
def shift_list(list_to_shift, number_to_shift, direction):
  new_list = copy.deepcopy(list_to_shift)
  for _ in range(0, number_to_shift):
    if direction == 'forward':
      # Insert the first item at the end of the list
      first_item = new_list[0]
      new_list.append(first_item)
      # Remove the first item
      new_list.pop(0)
    elif direction == 'back':
      # Insert the last item at the start of the list
      last_item = new_list[-1]
      new_list.insert(0, last_item)
      # Remove the last item
      new_list.pop()
  return new_list


# Fill key to specified length
def fill_key(key, length):
  newKey = key
  while len(newKey) < length:
    if (length - len(newKey)) >= len(key):
      newKey += key
    else:
      number_to_slice = int(float(length) % float(len(newKey)))
      newKey += key[:number_to_slice]
  return newKey


# Translate data
def vig_crypt(raw_string, user_key, crypt_base, operation):
  # Set up string to store translated message
  translated_msg = ''

  # Set up dict to determine shift direction
  shift_dirs = {
    'Encrypt': 'forward',
    'Decrypt': 'back',
  }

  # Run through string, translate message
  n = 0
  for letter in raw_string:
    # Find position of letter in cryptBase
    letter_pos = crypt_base.index(letter)

    # Find position of key letter in cryptBase
    key_letter_pos = crypt_base.index(user_key[n])

    # Create shifted cryptBase for this letter
    shifted_crypt_base = shift_list(crypt_base, key_letter_pos,
                                    shift_dirs[operation])

    # Get the translated letter, add to translated message
    translated_msg += shifted_crypt_base[letter_pos]

    # Increment n counter
    n += 1

  # Return decrypted string
  return f'{operation}ed message: {translated_msg}'


# Main function
def vigenere():
  # Ask user to encrypt/decrypt
  operation = input('Would you like to (e)ncrypt or (d)ecrypt? ').lower()

  # Gather string from user
  if operation in ['encrypt', 'e']:
    operation = 'Encrypt'
    string_crypt = input('Please enter a message to encrypt (no numbers): ')
  elif operation in ['decrypt', 'd']:
    operation = 'Decrypt'
    string_crypt = input('Please enter a message to decrypt: ')
  else:
    print('Please enter a valid operation.')
    quit()

  # Uppercase string and remove spaces
  string_crypt = string_crypt.upper().replace(" ", "")

  # Make translator objects to strip punctuation and digits
  remove_punctuation = str.maketrans('', '', string.punctuation)
  remove_digits = str.maketrans('', '', string.digits)

  # Strip punctuation and digits from string
  string_crypt = (string_crypt.translate(remove_punctuation)
                            .translate(remove_digits))

  # Ask user for key, make uppercase and remove spaces
  key = input('Please enter your key (a word): ').upper().replace(" ", "")

  # Repeat the key to match the length of the string
  key = fill_key(key, len(string_crypt))

  # Set up list of letters to use in crypto operations
  crypt_base = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  # Run translation
  return vig_crypt(string_crypt, key, crypt_base, operation)


# Call main function, print returned data
print(vigenere())
