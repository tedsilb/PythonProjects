"""This program will encrypt and decrypt messages using a Caesar cipher.
By Ted Silbernagel
"""

import enum
import string
from typing import List


class Operation(enum.Enum):
  ENCRYPT = enum.auto()
  DECRYPT = enum.auto()
  CRACK = enum.auto()


class CaesarCipher:
  crypt_base: List[str] = [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

  def parse_input(self, message: str) -> List[str]:
    return message.translate(str.maketrans(
        '', '', string.punctuation)).upper().split(' ')

  def encrypt(self, key: int, message: str) -> str:
    encrypted_words: List[str] = []

    for word in self.parse_input(message):
      current_word = ''
      for letter in word:
        current_index = self.crypt_base.index(letter) + 1
        new_index = (current_index + key) % 26
        new_index -= 1
        current_word += self.crypt_base[new_index]
      encrypted_words.append(current_word)

    return ' '.join(encrypted_words)

  def decrypt(self, key: int, message: str) -> str:
    decrypted_words: List[str] = []

    for word in self.parse_input(message):
      current_word = ''
      for letter in word:
        current_index = self.crypt_base.index(letter) + 1
        new_index = (current_index - key + 26) % 26
        new_index -= 1
        current_word += self.crypt_base[new_index]
      decrypted_words.append(current_word)

    return ' '.join(decrypted_words)

  def crack(self, message: str) -> str:
    print('Crack starting. Press enter to try again or any other key to exit.')

    # Try each combination
    for i in range(1, 27):
      cracked_words: List[str] = []

      # Run through list, crack words
      for word in self.parse_input(message):
        current_word = ''
        for letter in word:
          current_index = self.crypt_base.index(letter) + 1
          new_index = (current_index - i + 26) % 26
          new_index -= 1
          current_word += self.crypt_base[new_index]
        cracked_words.append(current_word)

      cracked_string = ' '.join(cracked_words)

      if (input(f'Attempt {i}/26: "{cracked_string}": Correct? ').lower()
          not in ['', 'n']):
        return cracked_string

    return 'Crack unsuccessful.'


def _gather_operation() -> Operation:
  operation_input = input(
      'Would you like to (e)ncrypt, (d)ecrypt, or (c)rack? ').lower()
  if operation_input in ['e', 'encrypt']:
    return Operation.ENCRYPT
  elif operation_input in ['d', 'decrypt']:
    return Operation.DECRYPT
  elif operation_input in ['c', 'crack']:
    return Operation.CRACK
  else:
    raise Exception('Invalid operation entered.')


def _gather_message(operation: Operation) -> str:
  return input(f'Please enter the message to {operation.name.lower()}: ')


def _gather_encryption_key() -> int:
  return int(input('Please enter the key to use (1 to 25): '))


if __name__ == '__main__':
  operation = _gather_operation()
  message = _gather_message(operation)
  if operation is Operation.ENCRYPT or operation is Operation.DECRYPT:
    encryption_key = _gather_encryption_key()

  cipher = CaesarCipher()

  if operation is Operation.ENCRYPT:
    response = cipher.encrypt(encryption_key, message)
  elif operation is Operation.DECRYPT:
    response = cipher.decrypt(encryption_key, message)
  elif operation is Operation.CRACK:
    response = cipher.crack(message)

  print(response)
