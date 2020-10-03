"""Calculates Pi using the Gregory-Leibniz series.
By Ted Silbernagel
"""

import decimal

# Set maximum decimal places
decimal.setcontext(decimal.Context(prec=100))


def gregory_leibniz(user_precision: int) -> decimal.Decimal:
  calculated_pi = decimal.Decimal(1.0)
  current_num = decimal.Decimal(3.0)

  for i in range(1, user_precision + 1):
    if not i % 100000:
      print(f'\rCalculating: ({i}/{user_precision})', end="")

    num_to_change = decimal.Decimal(1.0) / current_num

    if not i % 2:
      calculated_pi += num_to_change
    else:
      calculated_pi -= num_to_change
    current_num += decimal.Decimal(2.0)

  print('\n')

  return calculated_pi * decimal.Decimal(4.0)


if __name__ == '__main__':
  print('This program calculates pi to a specific precision '
        'using the Gregory-Leibniz series.')
  print('(Not the number of decimal places - the higher the precision, '
        'the more accurate the calculation will be)')

  user_no = int(
      input('Please enter the precision you\'d like '
            '(at least few hundred thousand): '))

  result: decimal.Decimal = gregory_leibniz(user_no)
  print('Result: ' + str(result))
