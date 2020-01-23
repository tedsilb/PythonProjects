"""Rock paper scissors game.
By Ted Silbernagel
"""

import random
from typing import Dict


def play_rps(user_choice: str) -> Dict[str, str]:
  # Parse user choice
  user_choice = user_choice.lower()
  if user_choice in ['r', 'rock']:
    usr_choice = 'rock'
  elif user_choice in ['p', 'paper']:
    usr_choice = 'paper'
  elif user_choice in ['s', 'scissors']:
    usr_choice = 'scissors'
  else:
    raise Exception(f'Invalid choice selected: {user_choice}')

  # Pick a random choice
  cpu_choice = random.choice(['rock', 'paper', 'scissors'])

  # Set up return values dict
  results = {
    'usr_choice': usr_choice,
    'cpu_choice': cpu_choice,
  }

  # Check to see who won, return it
  if usr_choice == cpu_choice:
    results['result'] = 'Tie.'
  elif (usr_choice == 'rock' and cpu_choice == 'scissors'
        or usr_choice == 'paper' and cpu_choice == 'rock'
        or usr_choice == 'scissors' and cpu_choice == 'paper'):
    results['result'] = 'You win!'
  else:
    results['result'] = 'You lose :('

  return results


# Call function, display results
print('Rock, paper, scissors!')
response = play_rps(input('Please select (r)ock, (p)aper, or (s)cissors: '))
print(f'You picked {response["usr_choice"]}, '
      f'the computer picked {response["cpu_choice"]}. {response["result"]}')
