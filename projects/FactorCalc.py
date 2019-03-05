# Calculates all factors of a number
# By Ted Silbernagel

# Import dependencies
from time import time

# Define function
def calcFactors(userNo):  
  # Get start time
  startTime = time()
  
  # Create array to store the factors in
  allFactors = []

  # Calculate factors
  for number in range(1, userNo + 1):
    if (userNo % number) == 0:
      allFactors.append(number)

  # Return data to user
  returnData = {}
  returnData['userNo'] = userNo
  returnData['allFactors'] = allFactors
  returnData['timeTaken'] = round(time() - startTime, 6)
  return returnData

# Get number from user
print('This program will calculate all factors of the number you specify.')
enteredNo = int(input('Please enter a number: '))

# Call function, print response
response = calcFactors(enteredNo)
print(f'All factors of {response["userNo"]}: {response["allFactors"]}')
print(f'Took {response["timeTaken"]}s.')