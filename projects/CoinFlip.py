# This program will flip a coin over and over, keeping track of heads/tails
# By Ted Silbernagel

# Import dependencies
import random

# Define function to check if a string is a number
def isNumber(nbr):
  try:
    int(nbr)
    return True
  except ValueError:
    return False

# Define function
def flipCoin():
  userQuit = False
  wantToQuit = ''
  heads = 0
  tails = 0
  timesToRun = 0
  while not userQuit:
    # Flip a coin, get the result
    flip = random.choice([True, False])
    # Add to counter
    if flip == True:
      heads += 1
      print('Heads.')
    else:
      tails += 1
      print('Tails.')
    # Tell user the current totals
    if heads == 0:
      if tails == 1:
        print('Totals: 0 heads, 1 tail')
      else:
        print(f'Totals: 0 heads, {tails} tails')
    elif heads == 1:
      if tails == 1:
        print('Totals: 1 head, 1 tail')
      else:
        print(f'Totals: 1 head, {tails} tails')
    else:
      if tails == 1:
        print(f'Totals: {heads} heads, 1 tail')
      else:
        print(f'Totals: {heads} heads, {tails} tails')
    # Subtract one from run times
    if timesToRun > 0:
      timesToRun -= 1
    # Ask user if they want to continue
    if timesToRun == 0:
      wantToQuit = input('Press q to quit, enter to continue: ')
    if wantToQuit.lower() == 'q':
      userQuit = True
    elif isNumber(wantToQuit):
      timesToRun = int(wantToQuit)
      wantToQuit = ''

# Call function
print('This program will flip a coin and keep track of how many heads/tails you got.')
flipCoin()