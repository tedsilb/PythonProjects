"""Find all prime numbers up to a given number.
Uses the Sieve of Eratosthenes algorithm.
By Ted Silbernagel
"""

import time
from typing import Dict, List, Union


def sieve(user_no: int) -> Dict[str, Union[List[int], float]]:
  start_time = time.time()
  numbers_list = list(range(1, user_no + 1))

  for number in numbers_list:
    if number > 1:
      for num_to_multiply in range(2, user_no // number):
        try:
          numbers_list.remove(number * num_to_multiply)
        except ValueError:
          pass

  return {
      'numbers_list': numbers_list,
      'timeTaken': round(time.time() - start_time, 6),
  }


# Gather number from user, run function
print('This program will find all primes up to a given number.')
response = sieve(int(input('Please enter a number: ')))
print(response['numbersList'])
print(f'Took {response["timeTaken"]}s.')
