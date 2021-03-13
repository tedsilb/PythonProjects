"""This program will allow for many mathematical operations on two numbers.
By Ted Silbernagel
"""

import enum
import sys
from typing import Tuple


class Operation(enum.Enum):
  ADD = enum.auto()
  SUBTRACT = enum.auto()
  MULTIPLY = enum.auto()
  DIVIDE = enum.auto()
  RAISE = enum.auto()
  MODULO = enum.auto()


def get_operation() -> Operation:
  """Gather and parse operation."""
  print('Calculator - please select what calculation you would like to perform:')
  print('  (A)dd two numbers')
  print('  (S)ubtract one number from another')
  print('  (M)ultiply two numbers')
  print('  (D)ivide one number by another')
  print('  (R)aise one number to the power of another')
  print('  Get the r(e)mainder of dividing one number by another')
  user_op = input('Please select a calculation: ').lower()

  # Parse method
  if user_op == 'a':
    return Operation.ADD
  elif user_op == 's':
    return Operation.SUBTRACT
  elif user_op == 'm':
    return Operation.MULTIPLY
  elif user_op == 'd':
    return Operation.DIVIDE
  elif user_op == 'r':
    return Operation.RAISE
  elif user_op == 'e':
    return Operation.MODULO
  else:
    print('No calculation selected. Exiting.')
    sys.exit()


def get_numbers(operation: Operation) -> Tuple[float, float]:
  """Gather numbers from user."""
  if operation is Operation.ADD:
    first_no = input('Enter first number to add: ')
    second_no = input('Enter second number to add: ')
  elif operation is Operation.SUBTRACT:
    first_no = input('Enter the number to subtract from: ')
    second_no = input('Enter the number to subtract: ')
  elif operation is Operation.MULTIPLY:
    first_no = input('Enter first number to multiply: ')
    second_no = input('Enter second number to multiply: ')
  elif operation is Operation.DIVIDE:
    first_no = input('Enter the number to divide (numerator): ')
    second_no = input('Enter the number to divide by (denominator): ')
  elif operation is Operation.RAISE:
    first_no = input('Enter the base number: ')
    second_no = input('Enter the number to raise to (exponent): ')
  elif operation is Operation.MODULO:
    first_no = input('Enter the number to divide (numerator): ')
    second_no = input('Enter the number to divide by (denominator): ')
  else:
    raise Exception(f'Incorrect operation entered: {operation}')
  return float(first_no), float(second_no)


def calculate(first_no: float, second_no: float, method: Operation) -> float:
  """Perform calculation based on operation."""
  if method is Operation.ADD:
    return first_no + second_no
  elif method is Operation.SUBTRACT:
    return first_no - second_no
  elif method is Operation.MULTIPLY:
    return first_no * second_no
  elif method is Operation.DIVIDE:
    return first_no / second_no
  elif method is Operation.RAISE:
    return first_no**second_no
  elif method is Operation.MODULO:
    return first_no % second_no
  else:
    raise NotImplementedError('Operation not supported.')


def print_result(first_no: float, second_no: float, result: float, operation: Operation) -> None:
  """Print numbers based on operation."""
  if operation is Operation.ADD:
    print(f'Calculated: {first_no} plus {second_no} equals {result}')
  elif operation is Operation.SUBTRACT:
    print(f'Calculated: {first_no} subtracted by {second_no} equals {result}')
  elif operation is Operation.MULTIPLY:
    print(f'Calculated: {first_no} times {second_no} equals {result}')
  elif operation is Operation.DIVIDE:
    print(f'Calculated: {first_no} divided by {second_no} equals {result}')
  elif operation is Operation.RAISE:
    print(f'Calculated: {first_no} raised to the power of {second_no} equals {result}')
  elif operation is Operation.MODULO:
    print(f'Calculated: The modulus of {first_no} divided by {second_no} equals {result}')


if __name__ == '__main__':
  operation = get_operation()
  first_no, second_no = get_numbers(operation)

  calculated_value = calculate(first_no, second_no, operation)

  print_result(first_no, second_no, calculated_value, operation)
