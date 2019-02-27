# Given a price, determine how many of each coin is needed to pay for it.
# By Ted Silbernagel

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
  numQ = math.floor(remainingValue / valueQ)

  # Subtract quarters from remaining value
  remainingValue -= (numQ * valueQ)

  # Determine number of dimes
  numD = math.floor(remainingValue / valueD)

  # Subtract dimes from remaining value
  remainingValue -= (numD * valueD)

  # Determine number of nickels
  numN = math.floor(remainingValue / valueN)

  # Subtract nickels from remaining value
  remainingValue -= (numN * valueN)

  # Determine number of pennies
  numP = math.floor(remainingValue / valueP)

  # Subtract pennies from remaining value
  remainingValue -= (numP * valueP)

  # Print values to console
  return f'For ${price}, you will need {numQ} quarters, {numD} dimes, {numN} nickels, and {numP} pennies.'

# Gather data from user
print('Please enter a price (no dollar sign), and this program will tell you what combination of coins you will need.')
userPrice = float(input('Enter price: '))

# Call function, print response
response = calcChange(userPrice)
print(response)