# Given the weights of types of coins, estimate the number of coins and the number of wrappers needed.

# Import dependencies
import math

# Define function
def estimateWeight(wgtP, wgtN, wgtD, wgtQ):
  # Parse arguments
  wgtP = float(wgtP)
  wgtN = float(wgtN)
  wgtD = float(wgtD)
  wgtQ = float(wgtQ)

  # Define values
  valPerP = 0.01
  valPerN = 0.05
  valPerD = 0.10
  valPerQ = 0.25

  # Define weights
  wgtPerP = 2.5
  wgtPerN = 5.0
  wgtPerD = 2.268
  wgtPerQ = 2.67

  # Define amounts per wrapper
  wrapperCapacityP = 50
  wrapperCapacityN = 40
  wrapperCapacityD = 50
  wrapperCapacityQ = 40

  # Calculate number of coins for each weight
  numP = wgtP / wgtPerP
  numN = wgtN / wgtPerN
  numD = wgtD / wgtPerD
  numQ = wgtQ / wgtPerQ

  # Parse number of coins to integers (round down)
  numP = math.floor(numP)
  numN = math.floor(numN)
  numD = math.floor(numD)
  numQ = math.floor(numQ)

  # Determine number of wrappers needed (round up)
  wrappersP = math.ceil(numP / wrapperCapacityP)
  wrappersN = math.ceil(numN / wrapperCapacityN)
  wrappersD = math.ceil(numD / wrapperCapacityD)
  wrappersQ = math.ceil(numQ / wrapperCapacityQ)

  # Determine value of currency
  valueP = numP * valPerP
  valueN = numN * valPerN
  valueD = numD * valPerD
  valueQ = numQ * valPerQ
  valueTotal = valueP + valueN + valueD + valueQ

  # Print a blank line before returning values
  print('')

  # Print the return values for the user
  # Pennies
  if (numP == 1):
    if (wrappersP == 1):
      print(f'You have {numP} penny, and you will need {wrappersP} wrapper for them.')
    else:
      print(f'You have {numP} penny, and you will need {wrappersP} wrappers for them.')
  else:
    if (wrappersP == 1):
      print(f'You have {numP} pennies, and you will need {wrappersP} wrapper for them.')
    else:
      print(f'You have {numP} pennies, and you will need {wrappersP} wrappers for them.')
  # Nickels
  if (numN == 1):
    if (wrappersN == 1):
      print(f'You have {numN} nickel, and you will need {wrappersN} wrapper for them.')
    else:
      print(f'You have {numN} nickel, and you will need {wrappersN} wrappers for them.')
  else:
    if (wrappersN == 1):
      print(f'You have {numN} nickels, and you will need {wrappersN} wrapper for them.')
    else:
      print(f'You have {numN} nickels, and you will need {wrappersN} wrappers for them.')
  # Dimes
  if (numD == 1):
    if (wrappersD == 1):
      print(f'You have {numD} dime, and you will need {wrappersD} wrapper for them.')
    else:
      print(f'You have {numD} dime, and you will need {wrappersD} wrappers for them.')
  else:
    if (wrappersD == 1):
      print(f'You have {numD} dimes, and you will need {wrappersD} wrapper for them.')
    else:
      print(f'You have {numD} dimes, and you will need {wrappersD} wrappers for them.')
  # Quarters
  if (numQ == 1):
    if (wrappersQ == 1):
      print(f'You have {numQ} quarter, and you will need {wrappersQ} wrapper for them.')
    else:
      print(f'You have {numQ} quarter, and you will need {wrappersQ} wrappers for them.')
  else:
    if (wrappersQ == 1):
      print(f'You have {numQ} quarters, and you will need {wrappersQ} wrapper for them.')
    else:
      print(f'You have {numQ} quarters, and you will need {wrappersQ} wrappers for them.')
  # Value of coins
  print(f'The total value of your coins is ${valueTotal}.')

# Gather data from users
print('Please enter the weights of your coins (in grams):')
usrWgtP = input('What is the weight of your pennies? ')
usrWgtN = input('What is the weight of your nickels? ')
usrWgtD = input('What is the weight of your dimes? ')
usrWgtQ = input('What is the weight of your quarters? ')

# Run function
estimateWeight(usrWgtP, usrWgtN, usrWgtD, usrWgtQ)