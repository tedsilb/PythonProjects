# Determine the mean, median, and mode for a list of numbers

# Define function
def centralTendency():
  # Prepare to gather numbers
  numbersList = []
  stopGathering = 0

  # Gather list of numbers from user
  while (stopGathering == 0):
    enteredNumber = input('Please enter a number (press enter to stop):')
    if (enteredNumber == ''):
      stopGathering = 1
    else:
      enteredNumber = float(enteredNumber)
      numbersList.append(enteredNumber)

  # Calculate sum of list
  listSum = 0
  for number in numbersList:
    listSum =+ number

  # Calculate mean
  listMean = listSum / len(numbersList)

  # Calculate median
