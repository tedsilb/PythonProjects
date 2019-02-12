# Determine the mean, median, and mode for a list of numbers

# Import dependencies
import math

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

  # Round mean based on user input
  roundTo = int(input('How many decimal places would you like to round the mean to? '))
  listMean = round(listMean, roundTo)

  # Calculate median
  medianList = numbersList
  medianList.sort()
  # Determine if list is even or odd length
  if (len(numbersList) % 2 == 0):
    # If it's even, grab the middle two numbers and average them
    medianTempNo1 = medianList[int(len(medianList) / 2)]
    medianTempNo2 = medianList[int((len(medianList) / 2) + 1)]
    listMedian = (medianTempNo1 + medianTempNo2) / 2
  else:
    # If it's odd, grab the middle number.
    listMedian = medianList[math.ceil(len(medianList) / 2)]

  # Calculate mode
  listMode = max(set(medianList), key=medianList.count)

  # Print data for user
  print(f'The mean of these numbers is {listMean}.')
  print(f'The median of these numbers is {listMedian}.')
  print(f'The mode of these numbers is {listMode}.')

# Call function
centralTendency()