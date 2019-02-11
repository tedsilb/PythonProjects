import random

# Set up dice-roll function
def rollDice(n):
  print('Rolling dice ' + str(n) + ' times...')
  for i in range(0, n):
    randomNo = random.randint(1, 6)
    print(randomNo)

rollDice(3)