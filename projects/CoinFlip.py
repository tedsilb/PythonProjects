# This program will flip a coin repeatedly, keeping track of heads and tails
# By Ted Silbernagel

import random


def isNumber(nbr) -> bool:
  try:
    int(nbr)
    return True
  except ValueError:
    return False


def flipCoin() -> None:
  userQuit = False
  wantToQuit = ''
  heads = 0
  tails = 0
  timesToRun = 0

  while not userQuit:
    # Flip a coin, get the result
    flip = random.choice([True, False])

    # Add to counter
    if flip:
      heads += 1
      print('Heads.')
    else:
      tails += 1
      print('Tails.')

    # Tell user the current totals
    if not heads:
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
    if not timesToRun:
      wantToQuit = input('Press q to quit, enter to continue: ')
    if wantToQuit.lower() == 'q':
      userQuit = True
    elif isNumber(wantToQuit):
      timesToRun = int(wantToQuit)
      wantToQuit = ''

# Call function
print('This program will flip a coin and keep track of '
      'how many heads/tails you got.')
flipCoin()
