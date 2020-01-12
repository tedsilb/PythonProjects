# Guessing game - try to guess the number
# By Ted Silbernagel

import random


def higher_lower() -> None:
  # Let the user know the game is starting, give instructions
  print('Guessing game!')
  print('  A whole number between 1 and 100 will randomly be chosen.')
  print('  Guess a number, and I will tell you if the real number '
        'is higher or lower.')

  # Generate the number
  number_to_guess = random.randint(1, 100)

  # Set up a variable to see if they guessed correctly
  guess_correct = False

  # Set up a variable to count how many guesses it took
  guesses = 0

  # Start the loop to let the user guess
  while not guess_correct:
    guessed_number = int(input('Guess a number: '))
    guesses += 1
    if guessed_number == number_to_guess:
      print(f'Correct! You got the number in {guesses} guesses.')
      guess_correct = True
    elif guessed_number > number_to_guess:
      print('Lower!')
    elif guessed_number < number_to_guess:
      print('Higher!')

higher_lower()
