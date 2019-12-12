# Given the weights of types of coins,
#   estimate the number of coins and the number of wrappers needed.
# By Ted Silbernagel

import math
from typing import Text


class Coin(object):
  def __init__(self, name: Text, pluralName: Text, valuePerCoin: float,
               weightPerCoin: float, totalWeight: float, wrapperCapacity: int):
    # mapped
    self.name = name
    self.pluralName = pluralName

    # calculated
    self.numberOfCoins = math.floor(totalWeight / weightPerCoin)
    self.wrappersNeeded = math.ceil(self.numberOfCoins / wrapperCapacity)
    self.value = self.numberOfCoins * valuePerCoin


def estimateWeight(wgtP: float, wgtN: float, wgtD: float, wgtQ: float) -> None:
  # Set up Coin objects, calculate number of coins
  p = Coin('penny', 'pennies',    0.01, 2.5,   wgtP, 50)
  n = Coin('nickel', 'nickels',   0.05, 5.0,   wgtN, 40)
  d = Coin('dime', 'dimes',       0.10, 2.268, wgtD, 50)
  q = Coin('quarter', 'quarters', 0.25, 2.67,  wgtQ, 40)

  # Print a blank line before returning values
  print('')

  # Print the values for the user
  for coin in [p, n, d, q]:
    if coin.numberOfCoins == 1:
      print(f'You have 1 {coin.name}, and you will need 1 wrapper for it.')
    elif coin.wrappersNeeded == 1:
      print(f'You have {coin.numberOfCoins} {coin.pluralName}, and you will '
            'need 1 wrapper for them.')
    else:
      print(f'You have {coin.numberOfCoins} {coin.pluralName}, and you will '
            f'need {coin.wrappersNeeded} wrappers for them.')

  # Total value of coins
  print('The total value of your coins is '
        f'${p.value + n.value + d.value + q.value}.')

# Gather data from user, call function
print('Please enter the weights of your coins (in grams):')
estimateWeight(
  float(input('What is the weight of your pennies? ')),
  float(input('What is the weight of your nickels? ')),
  float(input('What is the weight of your dimes? ')),
  float(input('What is the weight of your quarters? '))
)
