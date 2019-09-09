# Calculates pi to a certain degree of accuracy using the Gregory-Leibniz series

# Import dependencies
from decimal import setcontext, Context, Decimal

# Set maximum decimal places
setcontext(Context(prec=100))


# Set up function to calculate
def gregoryLeibniz(userPrecision):
  precision = int(userPrecision)
  calculatedPi = Decimal(1.0)
  currentNum = Decimal(3.0)
  for i in range(1, precision + 1):
    if not i % 100000:
      print(f'\rCalculating: ({i}/{precision})', end = "")
    numToChange = Decimal(1.0) / currentNum
    if not i % 2:
      calculatedPi += numToChange
    else:
      calculatedPi -= numToChange
    currentNum += Decimal(2.0)
  print('\n')
  return calculatedPi * Decimal(4.0)

# Get precision from user, call function
print('This program calculates pi to a specific precision using the Gregory-Leibniz series.')
print('(Not the number of decimal places - the higher the precision, the more accurate the calculation will be)')
print('Result: ' + gregoryLeibniz(input('Please enter the precision you\'d like (at least few hundred thousand): ')))
