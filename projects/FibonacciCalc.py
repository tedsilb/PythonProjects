"""Generate the nth term in the Fibonacci sequence.
By Ted Silbernagel
"""

import time
from typing import Dict


def fibonacci_gen(n_term: int) -> Dict[str, float]:
  # Get start time
  start_time = time.time()

  # Check to see if they picked 1, 2, or 3
  if n_term <= 3:
    if n_term == 1:
      fib_no = 0
    elif n_term in [2, 3]:
      fib_no = 1

  # Otherwise, will need to generate
  else:
    # Initialise the loop at 3
    prev_no1 = 0
    prev_no2 = 1
    fib_no = 1
    # Start the loop to generate the Fibonacci number
    for _ in range(3, n_term):
      prev_no1, prev_no2 = prev_no2, fib_no
      fib_no = prev_no1 + prev_no2

  return {
    'nTerm': n_term,
    'fib_no': fib_no,
    'timeTaken': round(time.time() - start_time, 6),
  }


# Get n term from user
print('This program will get you a specific number in the Fibonacci sequence.')
user_n_term = int(input('Please enter which number in the sequence '
                        'you would like: '))

# Call function, print response
response = fibonacci_gen(user_n_term)
last_digit = response['nTerm'] % 10
string_end = f'number in the Fibonacci sequence is {response["fibNo"]}'
if last_digit == 1:
  print(f'The {response["nTerm"]}st {string_end}')
elif last_digit == 2:
  print(f'The {response["nTerm"]}nd {string_end}')
elif last_digit == 3:
  print(f'The {response["nTerm"]}rd {string_end}')
else:
  print(f'The {response["nTerm"]}th {string_end}')
print(f'Took {response["timeTaken"]}s.')
