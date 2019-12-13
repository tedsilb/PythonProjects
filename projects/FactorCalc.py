# Calculates all factors of a number
# By Ted Silbernagel

import time
from typing import Text, Dict


def calcFactors(userNo: float) -> Dict[Text, float]:
  # Get start time
  startTime = time.time()

  # Create list to store the factors in
  allFactors = []

  # Calculate factors
  for number in range(1, userNo + 1):
    if not userNo % number:
      allFactors.append(number)

  # Return data to user
  return {
    'userNo': userNo,
    'allFactors': allFactors,
    'timeTaken': round(time.time() - startTime, 6),
  }

# Get number from user
print('This program will calculate all factors of the number you specify.')
enteredNo = float(input('Please enter a number: '))

# Call function, print response
response = calcFactors(enteredNo)
print(f'All factors of {response["userNo"]}: {response["allFactors"]}')
print(f'Took {response["timeTaken"]}s.')
