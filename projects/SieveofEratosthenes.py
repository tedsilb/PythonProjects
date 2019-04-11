# This program uses the Sieve of Eratosthenes algorithm to find all prime numbers up to a given number.
# By Ted Silbernagel

# Import dependencies
from time import time

# Define function
def sieveE(userNo):
  startTime = time()
  numToGen = int(userNo)
  numbersList = list(range(1, numToGen + 1))
  for number in numbersList:
    if number > 1:
      for numMult in range(2, int(numToGen / number)):
        try:
          numbersList.remove(number * numMult)
        except Exception:
          pass
      numbersList
  returnData = {}
  returnData['numbersList'] = numbersList
  returnData['timeTaken'] = round(time() - startTime, 6)
  return returnData

# Gather number from user, run function
print('This program will find all primes up to a given number.')
enteredNo = input('Please enter a number: ')
response = sieveE(enteredNo)
print(response['numbersList'])
print(f'Took {response["timeTaken"]}s.')
