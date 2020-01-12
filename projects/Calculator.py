# This program will allow for many mathematical operations on two numbers
# By Ted Silbernagel

from typing import Text, Tuple


def get_operation() -> Text:
  # Gather and parse operation
  print('Calculator - please select what calculation '
        'you would like to perform:')
  print('  (A)dd two numbers')
  print('  (S)ubtract one number from another')
  print('  (M)ultiply two numbers')
  print('  (D)ivide one number by another')
  print('  (R)aise one number to the power of another')
  print('  Get the r(e)mainder of dividing one number by another')
  user_op = input('Please select a calculation: ').lower()

  # Parse method
  if user_op == 'a':
    return 'add'
  elif user_op == 's':
    return 'subtract'
  elif user_op == 'm':
    return 'multiply'
  elif user_op == 'd':
    return 'divide'
  elif user_op == 'r':
    return 'raise'
  elif user_op == 'e':
    return 'modulo'
  else:
    print('No calculation selected. Exiting.')
    quit()


def get_numbers(operation: Text) -> Tuple[float, float]:
  # Gather numbers from user
  if operation == 'add':
    first_no = input('Enter first number to add: ')
    second_no = input('Enter second number to add: ')
  elif operation == 'subtract':
    first_no = input('Enter the number to subtract from: ')
    second_no = input('Enter the number to subtract: ')
  elif operation == 'multiply':
    first_no = input('Enter first number to multiply: ')
    second_no = input('Enter second number to multiply: ')
  elif operation == 'divide':
    first_no = input('Enter the number to divide (numerator): ')
    second_no = input('Enter the number to divide by (denominator): ')
  elif operation == 'raise':
    first_no = input('Enter the base number: ')
    second_no = input('Enter the number to raise to (exponent): ')
  elif operation == 'modulo':
    first_no = input('Enter the number to divide (numerator): ')
    second_no = input('Enter the number to divide by (denominator): ')
  return float(first_no), float(second_no)


def calculate(first_no: float, second_no: float, method: Text) -> float:
  if method == 'add':
    return first_no + second_no
  elif method == 'subtract':
    return first_no - second_no
  elif method == 'multiply':
    return first_no * second_no
  elif method == 'divide':
    return first_no / second_no
  elif method == 'raise':
    return first_no ** second_no
  elif method == 'modulo':
    return first_no % second_no


def print_result(first_no: float, second_no: float, result: float,
                 operation: Text) -> None:
  # Print numbers based on operation
  if operation == 'add':
    print(f'Calculated: {first_no} plus {second_no} equals {result}')
  elif operation == 'subtract':
    print(f'Calculated: {first_no} subtracted by {second_no} equals {result}')
  elif operation == 'multiply':
    print(f'Calculated: {first_no} times {second_no} equals {result}')
  elif operation == 'divide':
    print(f'Calculated: {first_no} divided by {second_no} equals {result}')
  elif operation == 'raise':
    print(f'Calculated: {first_no} raised to the power of {second_no} '
          f'equals {result}')
  elif operation == 'modulo':
    print(f'Calculated: The modulus of {first_no} divided by {second_no} '
          f'equals {result}')


def run_calculator() -> None:
  # Get method from user
  operation = get_operation()

  # Get numbers from user
  first_no, second_no = get_numbers(operation)

  # Call calculate function with user data
  calculated_value = calculate(first_no, second_no, operation)

  # Print return values for user
  print_result(first_no, second_no, calculated_value, operation)

# Call function
run_calculator()
