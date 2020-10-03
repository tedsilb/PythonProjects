"""Guessing game - try to guess the number
By Ted Silbernagel
"""

import random


def higher_lower() -> None:
  print('Guessing game!')
  print('  A whole number between 1 and 100 will randomly be chosen.')
  print('  Guess a number, and I will tell you if the real number '
        'is higher or lower.')

  number_to_guess = random.randint(1, 100)
  guess_correct = False
  guesses_taken = 0

  while not guess_correct:
    guessed_number = int(input('Guess a number: '))
    guesses_taken += 1
    if guessed_number == number_to_guess:
      print(f'Correct! You got the number in {guesses_taken} guesses.')
      guess_correct = True
    elif guessed_number > number_to_guess:
      print('Lower!')
    elif guessed_number < number_to_guess:
      print('Higher!')


if __name__ == '__main__':
  higher_lower()
