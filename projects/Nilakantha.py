# Calculates pi to a certain degree of accuracy using the Nilakantha series

# Import dependencies
from decimal import setcontext
from decimal import Context
from decimal import Decimal

# Set maximum decimal places
setcontext(Context(prec=100))


# Set up function to calculate
def nilakantha(user_precision):
  precision = int(user_precision)
  calculated_pi = Decimal(3.0)
  last_num = Decimal(2.0)
  for i in range(1, precision + 1):
    if not i % 100000:
      print(f'\rCalculating: ({i}/{precision})', end='')
    num_to_change = Decimal(4.0) / (last_num
                                    * (last_num + Decimal(1.0))
                                    * (last_num + Decimal(2.0)))
    if i % 2:
      calculated_pi += num_to_change
    else:
      calculated_pi -= num_to_change
    last_num += Decimal(2.0)
  print('\n')
  return calculated_pi

# Get precision from user, call function
print('This program calculates pi to a specific precision '
      'using the Nilakantha series.')
print('(Not the number of decimal places - the higher the precision, '
      'the more accurate the calculation will be)')
print('Result: '
      + nilakantha(input('Please enter the precision you\'d like: ')))
