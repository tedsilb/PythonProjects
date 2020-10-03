"""Calculates Pi to a certain degree of accuracy using the Nilakantha series.
By Ted Silbernagel
"""

import decimal

# Set maximum decimal places
decimal.setcontext(decimal.Context(prec=100))


def nilakantha(user_precision: int) -> decimal.Decimal:
  calculated_pi = decimal.Decimal(3.0)
  last_num = decimal.Decimal(2.0)

  for i in range(1, user_precision + 1):
    if not i % 100000:
      print(f'\rCalculating: ({i}/{user_precision})', end='')

    num_to_change = (decimal.Decimal(4.0) /
                     (last_num * (last_num + decimal.Decimal(1.0)) *
                      (last_num + decimal.Decimal(2.0))))

    if i % 2:
      calculated_pi += num_to_change
    else:
      calculated_pi -= num_to_change

    last_num += decimal.Decimal(2.0)

  print('\n')

  return calculated_pi


if __name__ == '__main__':
  print('This program calculates pi to a specific precision '
        'using the Nilakantha series.')
  print('(Not the number of decimal places - the higher the precision, '
        'the more accurate the calculation will be)')

  user_no = int(input('Please enter the precision you\'d like: '))

  result: decimal.Decimal = nilakantha(user_no)
  print('Result: ' + str(result))
