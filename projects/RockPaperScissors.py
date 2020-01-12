# Rock paper scissors game!
# By Ted Silbernagel

# Import dependencies
import random


# Define function for game
def play_rps(user_choice):
  # Parse user choice
  user_choice = user_choice.lower()
  if user_choice in ['r', 'rock']:
    usr_choice = 'rock'
  elif user_choice in ['p', 'paper']:
    usr_choice = 'paper'
  elif user_choice in ['s', 'scissors']:
    usr_choice = 'scissors'

  # Pick a random choice
  cpuChoice = random.choice(['rock', 'paper', 'scissors'])

  # Set up return values dict
  results = {
    'usr_choice': usr_choice,
    'cpuChoice': cpuChoice,
  }

  # Check to see who won, return it
  if usr_choice == cpuChoice:
    results['result'] = 'Tie.'
  elif (usr_choice == 'rock' and cpuChoice == 'scissors'
        or usr_choice == 'paper' and cpuChoice == 'rock'
        or usr_choice == 'scissors' and cpuChoice == 'paper'):
    results['result'] = 'You win!'
  else:
    results['result'] = 'You lose :('

  return results

# Call function, display results
print('Rock, paper, scissors!')
user_input = input('Please select (r)ock, (p)aper, or (s)cissors: ')
response = play_rps(user_input)
print(f'You picked {response["usrChoice"]}, '
      f'the computer picked {response["cpuChoice"]}. {response["result"]}')
