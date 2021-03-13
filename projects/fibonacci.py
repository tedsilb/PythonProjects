"""Generate the nth term in the Fibonacci sequence.
By Ted Silbernagel
"""

import time
from typing import Dict


def fibonacci_gen(n_term: int) -> Dict[str, float]:
  start_time = time.time()

  if n_term <= 3:
    if n_term == 1:
      fib_no = 0
    elif n_term in [2, 3]:
      fib_no = 1
  else:
    # Initialise the loop at 3
    prev_no1 = 0
    prev_no2 = 1
    fib_no = 1

    for _ in range(3, n_term):
      prev_no1, prev_no2 = prev_no2, fib_no
      fib_no = prev_no1 + prev_no2

  return {
      'n_term': n_term,
      'fib_no': fib_no,
      'time_taken': round(time.time() - start_time, 6),
  }


if __name__ == '__main__':
  print('This program will get you a specific number in the Fibonacci sequence.')
  user_n_term = int(input('Please enter which number in the sequence you would like: '))

  response = fibonacci_gen(user_n_term)
  last_digit = response['n_term'] % 10
  string_end = f'number in the Fibonacci sequence is {response["fib_no"]}'
  if last_digit == 1:
    print(f'The {response["n_term"]}st {string_end}')
  elif last_digit == 2:
    print(f'The {response["n_term"]}nd {string_end}')
  elif last_digit == 3:
    print(f'The {response["n_term"]}rd {string_end}')
  else:
    print(f'The {response["n_term"]}th {string_end}')
  print(f'Took {response["time_taken"]}s.')
