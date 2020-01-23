"""This program will flip a coin repeatedly, keeping track of heads and tails.
By Ted Silbernagel
"""

import random


def is_number(nbr: any) -> bool:
  try:
    int(nbr)
    return True
  except ValueError:
    return False


def flip_coin() -> None:
  user_quit = False
  want_to_quit = ''
  heads = 0
  tails = 0
  times_to_run = 0

  while not user_quit:
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
    if times_to_run > 0:
      times_to_run -= 1

    # Ask user if they want to continue
    if not times_to_run:
      want_to_quit = input('Press q to quit, enter to continue: ')
    if want_to_quit.lower() == 'q':
      user_quit = True
    elif is_number(want_to_quit):
      times_to_run = int(want_to_quit)
      want_to_quit = ''


# Call function
print('This program will flip a coin and keep track of '
      'how many heads/tails you got.')
flip_coin()
