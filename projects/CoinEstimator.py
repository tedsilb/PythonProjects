"""Estimate the number of coins and the number of wrappers needed for them.
By Ted Silbernagel
"""

import math


class Coin(object):

  def __init__(self, name: str, plural_name: str, value_per_coin: float,
               weight_per_coin: float, total_weight: float,
               wrapper_capacity: int):
    # Mapped
    self.name = name
    self.plural_name = plural_name

    # Calculated
    self.number_of_coins = math.floor(total_weight / weight_per_coin)
    self.wrappers_needed = math.ceil(self.number_of_coins / wrapper_capacity)
    self.value = self.number_of_coins * value_per_coin


def estimate_weight(wgt_p: float, wgt_n: float, wgt_d: float,
                    wgt_q: float) -> None:
  # Set up Coin objects, calculate number of coins
  p = Coin('penny', 'pennies', 0.01, 2.5, wgt_p, 50)
  n = Coin('nickel', 'nickels', 0.05, 5.0, wgt_n, 40)
  d = Coin('dime', 'dimes', 0.10, 2.268, wgt_d, 50)
  q = Coin('quarter', 'quarters', 0.25, 2.67, wgt_q, 40)

  # Print a blank line before returning values
  print('')

  # Print the values for the user
  for coin in [p, n, d, q]:
    if coin.number_of_coins == 1:
      print(f'You have 1 {coin.name}, and you will need 1 wrapper for it.')
    elif coin.wrappers_needed == 1:
      print(f'You have {coin.number_of_coins} {coin.plural_name}, and you will '
            'need 1 wrapper for them.')
    else:
      print(f'You have {coin.number_of_coins} {coin.plural_name}, and you will '
            f'need {coin.wrappers_needed} wrappers for them.')

  # Total value of coins
  print('The total value of your coins is '
        f'${p.value + n.value + d.value + q.value}.')


# Gather data from user, call function
print('Please enter the weights of your coins (in grams):')
estimate_weight(float(input('What is the weight of your pennies? ')),
                float(input('What is the weight of your nickels? ')),
                float(input('What is the weight of your dimes? ')),
                float(input('What is the weight of your quarters? ')))
