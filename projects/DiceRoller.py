# Roll a dice a certain number of times
# By Ted Silbernagel

import random


# Set up dice-roll function
def rollDice(n: int = 1, sides: int = 6) -> None:
  # Roll the dice!
  print(f'Rolling a {sides}-sided dice {n} time{"s" if n > 1 else ""}...')
  for _ in range(0, n):
    print(random.randint(1, sides))

# Gather data from user
userSides = int(input('How many sides would you like the dice to have? (default: 6) '))
userN = int(input('How many times would you like the dice to roll? (default: 1) '))

# Run the rollDice function based on user input.
rollDice(userN, userSides)
