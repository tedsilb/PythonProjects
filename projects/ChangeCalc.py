# Given a price, determine how many of each coin is needed to pay for it.
# By Ted Silbernagel

# Import dependencies
import math

from typing import Text


def calc_change(price: float) -> Text:
  # Set value of coins
  coin_values = {
    'q': 0.25,
    'd': 0.10,
    'n': 0.05,
    'p': 0.01,
  }

  # Set up dict to hold nums
  nums = {}

  # Set up variable to track how much is left to break out
  remaining_value = price

  for coin in coin_values.keys():
    # Determine number of coins
    nums[coin] = math.floor(remaining_value / coin_values[coin])
    # Subtract coin from remaining value
    remaining_value -= (nums[coin] * coin_values[coin])

  # Print values to console
  return (f'For ${price}, you will need {nums["q"]} quarters, '
          f'{nums["d"]} dimes, {nums["n"]} nickels, and {nums["p"]} pennies.')

# Gather data from user
print('Please enter a price (no dollar sign), and this program will tell you '
      'what combination of coins you will need.')
user_price = float(input('Enter price: '))

# Call function, print response
print(calc_change(user_price))
