"""Calculates all factors of a number.
By Ted Silbernagel
"""

import time
from typing import Dict


def calc_factors(user_no: int) -> Dict[str, float]:
  # Get start time
  start_time = time.time()

  # Create list to store the factors in
  all_factors = []

  # Calculate factors
  for number in range(1, user_no + 1):
    if not user_no % number:
      all_factors.append(number)

  return {
    'userNo': user_no,
    'all_factors': all_factors,
    'timeTaken': round(time.time() - start_time, 6),
  }


# Get number from user
print('This program will calculate all factors of the number you specify.')
entered_no = int(input('Please enter a number: '))

# Call function, print response
response = calc_factors(entered_no)
print(f'All factors of {response["userNo"]}: {response["allFactors"]}')
print(f'Took {response["timeTaken"]}s.')
