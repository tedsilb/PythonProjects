# Calculate descriptive statistics for a list of numbers
# By Ted Silbernagel

# Import dependencies
import math

# Define function to gather numbers
def gatherNumbers():
  # Prepare to gather numbers
  numbersList = []
  stopGathering = False

  # Gather list of numbers from user
  while stopGathering == False:
    enteredNumber = input('Please enter a number (press enter to stop): ')
    if enteredNumber == '':
      stopGathering = True
    else:
      enteredNumber = float(enteredNumber)
      numbersList.append(enteredNumber)
  return numbersList

# Define function to calculate stats
def descriptiveStats(numbersList):
  # Calculate mean
  listSum = 0
  for number in numbersList:
    listSum += number
  listMean = listSum / len(numbersList)

  # Round mean based on user input
  roundTo = int(input('How many decimal places would you like your numbers rounded to? '))
  listMean = round(listMean, roundTo)

  # Calculate median
  medianList = numbersList
  medianList.sort()
  # Determine if list is even or odd length
  if (len(numbersList) % 2) == 0:
    # If it's even, grab the middle two numbers and average them
    medianLower = medianList[int(len(medianList) / 2)]
    medianUpper = medianList[int((len(medianList) / 2) + 1)]
    listMedian = (medianLower + medianUpper) / 2
  else:
    # If it's odd, grab the middle number
    listMedian = medianList[math.ceil(len(medianList) / 2)]

  # Calculate mode
  listMode = max(set(medianList), key=medianList.count)

  # Calculate range
  listMin = min(numbersList)
  listMax = max(numbersList)

  # Calculate variance
  listSqDiffsFromMean = []
  for number in numbersList:
    listSqDiffsFromMean.append((number - listMean) ** 2)
  listVar = 0
  for sqDiff in listSqDiffsFromMean:
    listVar += sqDiff
  listVar = round(listVar / len(numbersList), roundTo)

  # Calculate standard deviation and standard error
  listStDev = round(listVar ** 0.5, roundTo)
  listStErr = round(listStDev / len(numbersList), roundTo)

  # Ask user for confidence interval
  confInt = int(input('Please enter a confidence interval (90, 95, 99): '))
  if confInt == 90:
    tStat = 1.64
  elif confInt == 95:
    tStat = 1.96
  elif confInt == 99:
    tStat = 2.58

  # Calculate confidence interval
  listLB = round(listMean - (tStat * listStErr), roundTo)
  listUB = round(listMean + (tStat * listStErr), roundTo)

  # Put data into a dictionary
  returnDict = {}
  returnDict['mean'] = listMean
  returnDict['median'] = listMedian
  returnDict['mode'] = listMode
  returnDict['min'] = listMin
  returnDict['max'] = listMax
  returnDict['variance'] = listVar
  returnDict['stDev'] = listStDev
  returnDict['stErr'] = listStErr
  returnDict['confInt'] = confInt
  returnDict['lowerBound'] = listLB
  returnDict['upperBound'] = listUB

  # Return data
  return returnDict

# Call function to gather numbers and calculate descriptive stats
response = descriptiveStats(gatherNumbers())

# Print data for user
print(f'Mean:     {response["mean"]}')
print(f'Median:   {response["median"]}')
print(f'Mode:     {response["mode"]}')
print(f'Range:    [{response["min"]}, {response["max"]}]')
print(f'Variance: {response["variance"]}')
print(f'Standard Deviation: {response["stDev"]}')
print(f'Standard Error:     {response["stErr"]}')
print(f'{response["confInt"]}% confidence interval:')
print(f'  Lower Bound: {response["lowerBound"]}')
print(f'  Upper Bound: {response["upperBound"]}')