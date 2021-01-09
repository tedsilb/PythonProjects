"""Calculates all factors of a number.
By Ted Silbernagel
"""

import time
from typing import Dict, List, Union


def calc_factors(user_no: int) -> Dict[str, Union[float, List[int]]]:
  start_time = time.time()
  all_factors = [number for number in range(1, user_no + 1) if not user_no % number]

  return {
      'user_no': user_no,
      'all_factors': all_factors,
      'time_taken': round(time.time() - start_time, 6),
  }


if __name__ == '__main__':
  print('This program will calculate all factors of the number you specify.')
  entered_no = int(input('Please enter a number: '))

  response = calc_factors(entered_no)
  print(f'All factors of {response["user_no"]}: {response["all_factors"]}')
  print(f'Took {response["time_taken"]}s.')
