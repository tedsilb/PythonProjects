# This program uses the Sieve of Eratosthenes algorithm to find
# all prime numbers up to a given number.
# By Ted Silbernagel

# Import dependencies
from time import time


# Define function
def sieve_e(user_no):
  start_time = time()
  num_to_gen = int(user_no)
  numbers_list = list(range(1, num_to_gen + 1))

  for number in numbers_list:
    if number > 1:
      for num_mult in range(2, num_to_gen // number):
        try:
          numbers_list.remove(number * num_mult)
        except ValueError:
          pass

  return  {
    'numbers_list': numbers_list,
    'timeTaken': round(time() - start_time, 6),
  }

# Gather number from user, run function
print('This program will find all primes up to a given number.')
response = sieve_e(input('Please enter a number: '))
print(response['numbersList'])
print(f'Took {response["timeTaken"]}s.')
