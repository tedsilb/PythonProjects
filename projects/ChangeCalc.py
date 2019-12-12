# Given a price, determine how many of each coin is needed to pay for it.
# By Ted Silbernagel

# Import dependencies
import math

from typing import Text


def calcChange(price: float) -> Text:
  # Set value of coins
  coinValues = {
    'q': 0.25,
    'd': 0.10,
    'n': 0.05,
    'p': 0.01,
  }

  # Set up dict to hold nums
  nums = {}

  # Set up variable to track how much is left to break out
  remainingValue = price

  for coin in coinValues.keys():
    # Determine number of coins
    nums[coin] = math.floor(remainingValue / coinValues[coin])
    # Subtract coin from remaining value
    remainingValue -= (nums[coin] * coinValues[coin])

  # Print values to console
  return (f'For ${price}, you will need {nums["q"]} quarters, '
          f'{nums["d"]} dimes, {nums["n"]} nickels, and {nums["p"]} pennies.')

# Gather data from user
print('Please enter a price (no dollar sign), and this program will tell you '
      'what combination of coins you will need.')
userPrice = float(input('Enter price: '))

# Call function, print response
print(calcChange(userPrice))
