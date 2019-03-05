# Generate the nth term in the Fibonacci sequence
# By Ted Silbernagel

# Import dependencies
from time import time

# Define function
def fibonacciGen(nTerm):
  # Get start time
  startTime = time()

  # Set up returnData object
  returnData = {}

  # Check to see if they picked 1 or 2
  if nTerm <= 3:
    if nTerm == 1:
      fibNo = 0
      returnData['nTerm'] = nTerm
      returnData['fibNo'] = fibNo
      returnData['timeTaken'] = round(time() - startTime, 6)

    elif nTerm == 2:
      fibNo = 1
      returnData['nTerm'] = nTerm
      returnData['fibNo'] = fibNo
      returnData['timeTaken'] = round(time() - startTime, 6)

    elif nTerm == 3:
      fibNo = 1
      returnData['nTerm'] = nTerm
      returnData['fibNo'] = fibNo
      returnData['timeTaken'] = round(time() - startTime, 6)

  # Otherwise will need to generate
  else:
    # Initialise the loop at 3
    prevNo1 = 0
    prevNo2 = 1
    fibNo = 1

    # Start the loop to generate the Fibonacci number
    for _ in range(3, nTerm):
      prevNo1 = prevNo2
      prevNo2 = fibNo
      fibNo = prevNo1 + prevNo2

    # Return calculation for user
    returnData['nTerm'] = nTerm
    returnData['fibNo'] = fibNo
    returnData['timeTaken'] = round(time() - startTime, 6)
  
  return returnData

# Get n term from user
print('This program will get you a specific number in the Fibonacci sequence.')
userNTerm = int(input('Please enter which number in the sequence you would like: '))

# Call function, print response
response = fibonacciGen(userNTerm)
if response['fibNo'] == 1:
  print(f'The {response["nTerm"]}st number in the Fibonacci sequence is {response["fibNo"]}')
elif response['fibNo'] == 2:
  print(f'The {response["nTerm"]}nd number in the Fibonacci sequence is {response["fibNo"]}')
elif response['fibNo'] == 3:
  print(f'The {response["nTerm"]}rd number in the Fibonacci sequence is {response["fibNo"]}')
else:
  print(f'The {response["nTerm"]}th number in the Fibonacci sequence is {response["fibNo"]}')
print(f'Took {response["timeTaken"]}s.')