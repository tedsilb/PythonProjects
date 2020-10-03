"""Given a price, determine how many coins are needed to total it.
By Ted Silbernagel
"""

import enum
import math


class Coin(enum.Enum):
  QUARTER = enum.auto()
  DIME = enum.auto()
  NICKEL = enum.auto()
  PENNY = enum.auto()


def calc_change(price: float) -> str:
  coins = {
      Coin.QUARTER: 0.25,
      Coin.DIME: 0.10,
      Coin.NICKEL: 0.05,
      Coin.PENNY: 0.01,
  }

  counts = {
      Coin.QUARTER: 0,
      Coin.DIME: 0,
      Coin.NICKEL: 0,
      Coin.PENNY: 0,
  }

  remaining_value = price

  for coin, amount in coins:
    # Determine how many of this coin goes into the value cleanly
    # Example: for $1.32, the quarter goes into it 5 times (5 * .25 = 1.25)
    counts[coin] = math.floor(remaining_value / amount)

    # Subtract the count from the remaining value
    remaining_value -= (counts[coin] * amount)

  return (f'For ${price}, you will need '
          f'{counts[Coin.QUARTER]} quarters, '
          f'{counts[Coin.DIME]} dimes, '
          f'{counts[Coin.NICKEL]} nickels, '
          f'and {counts[Coin.PENNY]} pennies.')


if __name__ == '__main__':
  print('Please enter a price (no dollar sign), and this program will tell you '
        'what combination of coins you will need.')
  user_price = float(input('Enter price: '))

  response: str = calc_change(user_price)
  print(response)
