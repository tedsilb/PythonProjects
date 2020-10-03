"""Find all prime numbers up to a given number.
Uses the Sieve of Eratosthenes algorithm.
By Ted Silbernagel
"""

import time
from typing import Dict, List, Union


def sieve(user_no: int) -> Dict[str, Union[List[int], float]]:
  start_time = time.time()
  numbers = list(range(1, user_no + 1))

  for number in numbers:
    if number > 1:
      for num_to_multiply in range(2, user_no // number):
        try:
          numbers.remove(number * num_to_multiply)
        except ValueError:
          pass

  return {
      'numbers': numbers,
      'time_taken': round(time.time() - start_time, 6),
  }


if __name__ == '__main__':
  print('This program will find all primes up to a given number.')

  user_no = int(input('Please enter a number: '))

  response = sieve(user_no)
  print(response['numbers'])
  print(f'Took {response["time_taken"]}s.')
