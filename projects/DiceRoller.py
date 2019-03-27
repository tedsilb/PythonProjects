# Roll a dice a certain number of times
# By Ted Silbernagel

# Import the random function to generate our numbers
import random

# Set up dice-roll function
def rollDice(n=1):  # default to 1 if they dont say how many times to run
  print('Rolling dice ' + str(n) + ' times...')
  for _ in range(0, n):
    randomNo = random.randint(1, 6)
    print(randomNo)

# Run the rollDice function three times.
rollDice(3)
