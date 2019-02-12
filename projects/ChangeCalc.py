# Given a price, determine how many of each coin is needed to pay for it.

# Import dependencies
import math

# Define function
def calcChange(price):
  # Set value of coins
  valueQ = 0.25
  valueD = 0.10
  valueN = 0.05
  valueP = 0.01

  # Set up variable to track how much is left to break out
  remainingValue = price

  # Determine number of quarters
  numQ = math.floor(price / valueQ)

  # Subtract quarters from remaining value
  remainingValue -= (numQ * valueQ)