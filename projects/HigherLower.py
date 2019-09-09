# Guessing game - try to guess the number
# By Ted Silbernagel

# Import dependencies
import random


# Define function
def higherLower():
  # Let the user know the game is starting, give instructions
  print('Guessing game!')
  print('  A number between 1 and 100 will randomly be chosen.')
  print('  Guess a number, and I will tell you if the real number is higher or lower.')

  # Generate the number
  numberToGuess = random.randint(1, 100)

  # Set up a variable to see if they guessed correctly
  guessCorrect = False

  # Set up a variable to count how many guesses it took
  guesses = 0

  # Start the loop to let the user guess
  while guessCorrect == False:
    guessedNumber = int(input('Guess a number: '))
    guesses += 1
    if guessedNumber == numberToGuess:
      print(f'Correct! You got the number in {guesses} guesses.')
      guessCorrect = True
    elif guessedNumber > numberToGuess:
      print('Lower!')
    elif guessedNumber < numberToGuess:
      print('Higher!')

# Call the function
higherLower()
