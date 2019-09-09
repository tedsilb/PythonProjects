
# Import dependencies
import random


# Define function for game
def playRPS(userChoice):
  # Parse user choice
  userChoice = userChoice.lower()
  if userChoice in ['r', 'rock']:
    usrChoice = 'rock'
  elif userChoice in ['p', 'paper']:
    usrChoice = 'paper'
  elif userChoice in ['s', 'scissors']:
    usrChoice = 'scissors'

  # List of choices for computer
  choices = ['rock', 'paper', 'scissors']

  # Pick a random choice
  cpuChoice = random.choice(choices)

  # Set up return values dict
  results = {
    'usrChoice': usrChoice,
    'cpuChoice': cpuChoice,
  }

  # Check to see who won, return it
  if usrChoice == cpuChoice:
    results['result'] = 'Tie.'
  elif (usrChoice == 'rock' and cpuChoice == 'scissors'
        or usrChoice == 'paper' and cpuChoice == 'rock'
        or usrChoice == 'scissors' and cpuChoice == 'paper'):
    results['result'] = 'You win!'
  else:
    results['result'] = 'You lose :('

  return results

# Call function, display results
print('Rock, paper, scissors!')
userInput = input('Please select (r)ock, (p)aper, or (s)cissors: ')
response = playRPS(userInput)
print(f'You picked {response["usrChoice"]}, the computer picked {response["cpuChoice"]}. {response["result"]}')
