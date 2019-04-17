# Calculates pi to a certain degree of accuracy using the Nilakantha series

# Import dependencies
from decimal import setcontext, Context, Decimal

# Set maximum decimal places
setcontext(Context(prec=100))

# Set up function to calculate
def nilakantha(userPrecision):
  precision = int(userPrecision)
  calculatedPi = Decimal(3.0)
  lastNum = Decimal(2.0)
  for i in range(1, precision + 1):
    if not i % 100000:
      print(f'\rCalculating: ({i}/{precision})', end = "")
    numToChange = Decimal(4.0) / (lastNum * (lastNum + Decimal(1.0)) * (lastNum + Decimal(2.0)))
    if i % 2:
      calculatedPi += numToChange
    else:
      calculatedPi -= numToChange
    lastNum += Decimal(2.0)
  print('\n')
  return calculatedPi

# Get precision from user, call function
print('This program calculates pi to a specific precision using the Nilakantha series.')
print('(Not the number of decimal places - the higher the precision, the more accurate the calculation will be)')
response = nilakantha(input('Please enter the precision you\'d like: '))
print(f'Result: {response}')
