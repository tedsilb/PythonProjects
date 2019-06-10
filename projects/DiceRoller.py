# Roll a dice a certain number of times
# By Ted Silbernagel

# Import the random function to generate our numbers
import random

# Set up dice-roll function
def rollDice(n, sides):  # default to 1 if they dont say how many times to run
  # Parse user input
  try:
    n = int(n)
  except ValueError:
    n = 1
  try:
    sides = int(sides)
  except:
    sides = 6

  # Roll the dice!
  if n == 1:
    print(f'Rolling a {str(sides)}-sided dice {str(n)} time...')
  else:
    print(f'Rolling a {str(sides)}-sided dice {str(n)} times...')
  for _ in range(0, n):
    randomNo = random.randint(1, sides)
    print(randomNo)

# Gather data from user
userSides = input('How many sides would you like the dice to have? (default: 6) ')
userN = input('How many times would you like the dice to roll? (default: 1) ')

# Run the rollDice function based on user input.
rollDice(userN, userSides)
