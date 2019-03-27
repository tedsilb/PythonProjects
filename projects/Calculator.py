# This program will allow for many mathematical operations on two numbers
# By Ted Silbernagel

def calculate(firstNo, secondNo, method):
  # Parse data and return calculated value
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

def runCalculator():
  # Gather method from user
  print('Calculator - please select what calculation you would like to perform:')
  print('  (A)dd two numbers')
  print('  (S)ubtract one number from another')
  print('  (M)ultiply two numbers')
  print('  (D)ivide one number by another')
  print('  (R)aise one number to the power of another')
  print('  Get the r(e)mainder of dividing one number by another')
  methodSelection = input('Please select a calculation: ')
  methodSelection = methodSelection.lower()

  # Parse method
  if methodSelection == 'a':
    selectedMethod = 'add'
  elif methodSelection == 's':
    selectedMethod = 'subtract'
  elif methodSelection == 'm':
    selectedMethod = 'multiply'
  elif methodSelection == 'd':
    selectedMethod = 'divide'
  elif methodSelection == 'r':
    selectedMethod = 'raise'
  elif methodSelection == 'e':
    selectedMethod = 'modulo'
  else:
    print('No calculation selected. Exiting.')
    quit()

  # Gather numbers from user
  if selectedMethod == 'add':
    firstNo = input('Enter first number to add: ')
    secondNo = input('Enter second number to add: ')
  elif selectedMethod == 'subtract':
    firstNo = input('Enter the number to subtract from: ')
    secondNo = input('Enter the number to subtract: ')
  elif selectedMethod == 'multiply':
    firstNo = input('Enter first number to multiply: ')
    secondNo = input('Enter second number to multiply: ')
  elif selectedMethod == 'divide':
    firstNo = input('Enter the number to divide (numerator): ')
    secondNo = input('Enter the number to divide by (denominator): ')
  elif selectedMethod == 'raise':
    firstNo = input('Enter the base number: ')
    secondNo = input('Enter the number to raise to (exponent): ')
  elif selectedMethod == 'modulo':
    firstNo = input('Enter the number to divide (numerator): ')
    secondNo = input('Enter the number to divide by (denominator): ')

  # Parse numbers to float
  firstNo = float(firstNo)
  secondNo = float(secondNo)

  # Call calculate function with user data
  calculatedValue = calculate(firstNo, secondNo, selectedMethod)

  # Convert number to int if it's an int
  if firstNo.is_integer():
    firstNo = int(firstNo)
  if secondNo.is_integer():
    secondNo = int(secondNo)
  if calculatedValue.is_integer():
    calculatedValue = int(calculatedValue)

  # Print return value for user
  if selectedMethod == 'add':
    print(f'Calculated: {firstNo} plus {secondNo} equals {calculatedValue}')
  elif selectedMethod == 'subtract':
    print(f'Calculated: {firstNo} subtracted by {secondNo} equals {calculatedValue}')
  elif selectedMethod == 'multiply':
    print(f'Calculated: {firstNo} times {secondNo} equals {calculatedValue}')
  elif selectedMethod == 'divide':
    print(f'Calculated: {firstNo} divided by {secondNo} equals {calculatedValue}')
  elif selectedMethod == 'raise':
    print(f'Calculated: {firstNo} raised to the power of {secondNo} equals {calculatedValue}')
  elif selectedMethod == 'modulo':
    print(f'Calculated: The modulus of {firstNo} divided by {secondNo} equals {calculatedValue}')

# Call function
runCalculator()
