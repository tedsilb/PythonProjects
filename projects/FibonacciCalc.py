# Generate the nth term in the Fibonacci sequence
# By Ted Silbernagel

# Import dependencies
from time import time


# Define function
def fibonacciGen(nTerm):
  # Get start time
  startTime = time()

  # Check to see if they picked 1, 2, or 3
  if nTerm <= 3:
    if nTerm == 1:
      fibNo = 0
    elif nTerm in [2, 3]:
      fibNo = 1
  # Otherwise will need to generate
  else:
    # Initialise the loop at 3
    prevNo1 = 0
    prevNo2 = 1
    fibNo = 1
    # Start the loop to generate the Fibonacci number
    for _ in range(3, nTerm):
      prevNo1, prevNo2 = prevNo2, fibNo
      fibNo = prevNo1 + prevNo2

  # Return calculation for user
  return {
    'nTerm': nTerm,
    'fibNo': fibNo,
    'timeTaken': round(time() - startTime, 6),
  }

# Get n term from user
print('This program will get you a specific number in the Fibonacci sequence.')
userNTerm = int(input('Please enter which number in the sequence you would like: '))

# Call function, print response
response = fibonacciGen(userNTerm)
lastDigit = response['nTerm'] % 10
stringEnd = f'number in the Fibonacci sequence is {response["fibNo"]}'
if lastDigit == 1:
  print(f'The {response["nTerm"]}st {stringEnd}')
elif lastDigit == 2:
  print(f'The {response["nTerm"]}nd {stringEnd}')
elif lastDigit == 3:
  print(f'The {response["nTerm"]}rd {stringEnd}')
else:
  print(f'The {response["nTerm"]}th {stringEnd}')
print(f'Took {response["timeTaken"]}s.')
