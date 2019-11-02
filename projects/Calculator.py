# This program will allow for many mathematical operations on two numbers
# By Ted Silbernagel


def getOperation():
  # Gather and parse operation
  print('Calculator - please select what calculation you would like to perform:')
  print('  (A)dd two numbers')
  print('  (S)ubtract one number from another')
  print('  (M)ultiply two numbers')
  print('  (D)ivide one number by another')
  print('  (R)aise one number to the power of another')
  print('  Get the r(e)mainder of dividing one number by another')
  userOp = input('Please select a calculation: ').lower()

  # Parse method
  if userOp == 'a':
    return 'add'
  elif userOp == 's':
    return 'subtract'
  elif userOp == 'm':
    return 'multiply'
  elif userOp == 'd':
    return 'divide'
  elif userOp == 'r':
    return 'raise'
  elif userOp == 'e':
    return 'modulo'
  else:
    print('No calculation selected. Exiting.')
    quit()


def getNumbers(operation):
  # Gather numbers from user
  if operation == 'add':
    firstNo = input('Enter first number to add: ')
    secondNo = input('Enter second number to add: ')
  elif operation == 'subtract':
    firstNo = input('Enter the number to subtract from: ')
    secondNo = input('Enter the number to subtract: ')
  elif operation == 'multiply':
    firstNo = input('Enter first number to multiply: ')
    secondNo = input('Enter second number to multiply: ')
  elif operation == 'divide':
    firstNo = input('Enter the number to divide (numerator): ')
    secondNo = input('Enter the number to divide by (denominator): ')
  elif operation == 'raise':
    firstNo = input('Enter the base number: ')
    secondNo = input('Enter the number to raise to (exponent): ')
  elif operation == 'modulo':
    firstNo = input('Enter the number to divide (numerator): ')
    secondNo = input('Enter the number to divide by (denominator): ')
  return float(firstNo), float(secondNo)


def calculate(firstNo, secondNo, method):
  if method == 'add':
    return firstNo + secondNo
  elif method == 'subtract':
    return firstNo - secondNo
  elif method == 'multiply':
    return firstNo * secondNo
  elif method == 'divide':
    return firstNo / secondNo
  elif method == 'raise':
    return firstNo ** secondNo
  elif method == 'modulo':
    return firstNo % secondNo


def printResult(firstNo, secondNo, result, operation):
  # Print numbers based on operation
  if operation == 'add':
    print(f'Calculated: {firstNo} plus {secondNo} equals {result}')
  elif operation == 'subtract':
    print(f'Calculated: {firstNo} subtracted by {secondNo} equals {result}')
  elif operation == 'multiply':
    print(f'Calculated: {firstNo} times {secondNo} equals {result}')
  elif operation == 'divide':
    print(f'Calculated: {firstNo} divided by {secondNo} equals {result}')
  elif operation == 'raise':
    print(f'Calculated: {firstNo} raised to the power of {secondNo} equals {result}')
  elif operation == 'modulo':
    print(f'Calculated: The modulus of {firstNo} divided by {secondNo} equals {result}')


def runCalculator():
  # Get method from user
  operation = getOperation()

  # Get numbers from user
  firstNo, secondNo = getNumbers(operation)

  # Call calculate function with user data
  calculatedValue = calculate(firstNo, secondNo, operation)

  # Convert numbers to ints if they're ints
  if not firstNo % 1:
    firstNo = int(firstNo)
  if not secondNo % 1:
    secondNo = int(secondNo)
  if not calculatedValue % 1:
    calculatedValue = int(calculatedValue)

  # Print return values for user
  printResult(firstNo, secondNo, calculatedValue, operation)

# Call function
runCalculator()
