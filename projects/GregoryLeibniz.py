# Calculates pi to a certain degree of accuracy using the Gregory-Leibniz series

import decimal

# Set maximum decimal places
decimal.setcontext(decimal.Context(prec=100))


# Set up function to calculate
def gregoryLeibniz(userPrecision: float) -> decimal.Decimal:
  calculatedPi = decimal.Decimal(1.0)
  currentNum = decimal.Decimal(3.0)
  for i in range(1, userPrecision + 1):
    if not i % 100000:
      print(f'\rCalculating: ({i}/{userPrecision})', end = "")
    numToChange = decimal.Decimal(1.0) / currentNum
    if not i % 2:
      calculatedPi += numToChange
    else:
      calculatedPi -= numToChange
    currentNum += decimal.Decimal(2.0)
  print('\n')
  return calculatedPi * decimal.Decimal(4.0)

# Get precision from user, call function
print('This program calculates pi to a specific precision '
      'using the Gregory-Leibniz series.')
print('(Not the number of decimal places - the higher the precision, '
      'the more accurate the calculation will be)')
userNo = float(input('Please enter the precision you\'d like '
                     '(at least few hundred thousand): '))
print('Result: ' + gregoryLeibniz(userNo))
