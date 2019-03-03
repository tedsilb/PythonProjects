# A rock paper scissors game

# Import dependencies
import random

# Define function for game
def playRPS(userChoice):
  # Parse user choice
  userChoice = userChoice.lower()
  if userChoice == 'r' or userChoice == 'rock':
    usrChoice = 'rock'
  elif userChoice == 'p' or userChoice == 'paper':
    usrChoice = 'paper'
  elif userChoice == 's' or userChoice == 'scissors':
    usrChoice = 'scissors'
  
  # List of choices for computer
  choices = ['rock', 'paper', 'scissors']

  # Pick a random choice
  cpuChoice = random.choice(choices)

  # Set up return values dict
  results = {}
  results['usrChoice'] = usrChoice
  results['cpuChoice'] = cpuChoice

  # Check to see who won, return it
  if usrChoice == 'rock':
    if cpuChoice == 'scissors':
      results['result'] = 'You win!'
    elif cpuChoice == 'p':
      results['result'] = 'You lose :('
    else:
      results['result'] = 'Tie.'
  elif usrChoice == 'paper':
    if cpuChoice == 'rock':
      results['result'] = 'You win!'
    elif cpuChoice == 'scissors':
      results['result'] = 'You lose :('
    else:
      results['result'] = 'Tie.'
  elif usrChoice == 'scissors':
    if cpuChoice == 'paper':
      results['result'] = 'You win!'
    elif cpuChoice == 'rock':
      results['result'] = 'You lose :('
    else:
      results['result'] = 'Tie.'
  
  return results

# Call function, display results
print('Rock, paper, scissors!')
userInput = input('Please select (r)ock, (p)aper, or (s)cissors: ')
response = playRPS(userInput)
print(f'You picked {response["usrChoice"]}, the computer picked {response["cpuChoice"]}. {response["result"]}')