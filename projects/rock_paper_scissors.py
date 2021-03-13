"""Rock paper scissors game.
By Ted Silbernagel
"""

import enum
import random
from typing import Dict


class Choice(enum.Enum):
  ROCK = enum.auto()
  PAPER = enum.auto()
  SCISSORS = enum.auto()


def _parse_choice(choice_str: str) -> Choice:
  if choice_str in ['r', 'rock']:
    return Choice.ROCK
  elif choice_str in ['p', 'paper']:
    return Choice.PAPER
  elif choice_str in ['s', 'scissors']:
    return Choice.SCISSORS
  else:
    raise Exception(f'Invalid choice selected: {choice_str}')


def play_rps(choice_str: str) -> Dict[str, str]:
  user_choice = _parse_choice(choice_str.lower())
  cpu_choice = random.choice([Choice.ROCK, Choice.PAPER, Choice.SCISSORS])

  if user_choice == cpu_choice:
    result = 'Tie.'
  elif (user_choice == Choice.ROCK and cpu_choice == Choice.SCISSORS or
        user_choice == Choice.PAPER and cpu_choice == Choice.ROCK or
        user_choice == Choice.SCISSORS and cpu_choice == Choice.PAPER):
    result = 'You win!'
  else:
    result = 'You lose :('

  return {
      'user_choice': user_choice.name.lower(),
      'cpu_choice': cpu_choice.name.lower(),
      'result': result,
  }


if __name__ == '__main__':
  print('Rock, paper, scissors!')
  choice = input('Please select (r)ock, (p)aper, or (s)cissors: ')
  response = play_rps(choice)
  print(f'You picked {response["user_choice"]}, '
        f'the computer picked {response["cpu_choice"]}. {response["result"]}')
