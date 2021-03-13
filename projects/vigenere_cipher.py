"""This program will encrypt and decrypt messages using a Vigenere cipher.
By Ted Silbernagel
"""

import copy
import enum
import string
from typing import List


class Operation(enum.Enum):
  ENCRYPT = enum.auto()
  DECRYPT = enum.auto()


class Direction(enum.Enum):
  FORWARD = enum.auto()
  BACKWARD = enum.auto()


class VigenereCipher:
  crypt_base: List[str] = [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

  def crypt(self, operation: Operation, key: str, message: str):
    """Encrypt/decrypt data."""
    key = self._prepare_key(key, len(message))
    message = self._prepare_message(message)
    shift_dir = self._get_shift_dir(operation)

    translated_msg = ''

    n = 0
    for letter in message:
      # Find position of letter in crypt_base
      letter_pos = self.crypt_base.index(letter)

      # Find position of key letter in crypt_base
      key_letter_pos = self.crypt_base.index(key[n])

      # Create shifted crypt_base for this letter
      shifted_crypt_base = self._shift_list(self.crypt_base, key_letter_pos, shift_dir)

      # Get the translated letter, add to the translated message
      translated_msg += shifted_crypt_base[letter_pos]

      # Increment n counter
      n += 1

    return f'{operation.name.capitalize()}ed message: {translated_msg}'

  def _prepare_key(self, key: str, length: int) -> str:
    return self._fill_key(key.upper().replace(" ", ""), length)

  def _prepare_message(self, message: str) -> str:
    upper_message = message.upper().replace(" ", "")
    remove_punctuation = str.maketrans('', '', string.punctuation)
    remove_digits = str.maketrans('', '', string.digits)
    return upper_message.translate(remove_punctuation).translate(remove_digits)

  @staticmethod
  def _shift_list(list_to_shift: List[str], shift_n: int, direction: Direction) -> List[str]:
    """Shift list a certain number of times."""
    new_list = copy.deepcopy(list_to_shift)
    for _ in range(0, shift_n):
      if direction is Direction.FORWARD:
        # Insert the first item at the end of the list
        first_item = new_list[0]
        new_list.append(first_item)
        # Remove the first item
        new_list.pop(0)
      elif direction is Direction.BACKWARD:
        # Insert the last item at the start of the list
        last_item = new_list[-1]
        new_list.insert(0, last_item)
        # Remove the last item
        new_list.pop()

    return new_list

  @staticmethod
  def _fill_key(key: str, length: int) -> str:
    """Fill key to the specified length."""
    new_key = key
    while len(new_key) < length:
      if (length - len(new_key)) >= len(key):
        new_key += key
      else:
        number_to_slice = int(float(length) % float(len(new_key)))
        new_key += key[:number_to_slice]

    return new_key

  @staticmethod
  def _get_shift_dir(operation: Operation) -> Direction:
    return {
        Operation.ENCRYPT: Direction.FORWARD,
        Operation.DECRYPT: Direction.BACKWARD,
    }[operation]


def _gather_operation() -> Operation:
  operation_input = input('Would you like to (e)ncrypt or (d)ecrypt? ').lower()
  if operation_input in ['e', 'encrypt']:
    return Operation.ENCRYPT
  elif operation_input in ['d', 'decrypt']:
    return Operation.DECRYPT
  else:
    raise Exception('Invalid operation entered.')


def _gather_message(operation: Operation) -> str:
  return input(f'Please enter the message to {operation.name.lower()}: ')


def _gather_encryption_key() -> str:
  return input('Please enter your key (a word): ')


if __name__ == '__main__':
  operation: Operation = _gather_operation()
  message: str = _gather_message(operation)
  encryption_key: str = _gather_encryption_key()

  cipher = VigenereCipher()

  response = cipher.crypt(operation, encryption_key, message)
  print(response)
