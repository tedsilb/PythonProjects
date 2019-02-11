# Goal 
#   Create a program that allows the user to input the total weight of each type of coin they have 
#   (pennies, nickels, dimes, and quarters), 
#   and then print out how many of each type of wrapper they would need, 
#   how many coins they have, and the estimated total value of all of their money.
#   Weight of each coin and how many fit inside each type of wrapper.
# Subgoals
#   Round all numbers printed out to the nearest whole number.
#   Allow the user to select whether they want to submit the weight in either grams or pounds.

def estimateWeight(wgtP, wgtN, wgtD, wgtQ):
  # Parse arguments
  wgtP = float(wgtP)
  wgtN = float(wgtN)
  wgtD = float(wgtD)
  wgtQ = float(wgtQ)
  
  # Define values
  valPerP = 0.01
  valPerN = 0.05
  valPerD = 0.10
  valPerQ = 0.25

  # Define weights 
  wgtPerP = 2.5
  wgtPerN = 5.0
  wgtPerD = 2.268
  wgtPerQ = 2.67

  # Define amounts per wrapper
  wrapperCapacityP = 50
  wrapperCapacityN = 40
  wrapperCapacityD = 50
  wrapperCapacityQ = 40

  # Calculate number of coins for each weight
  numP = wgtP / wgtPerP
  numN = wgtN / wgtPerN
  numD = wgtD / wgtPerD
  numQ = wgtQ / wgtPerQ

  # Parse number of coints to integers
  numP = int(numP)
  numN = int(numN)
  numD = int(numD)
  numQ = int(numQ)

  # Determine number of wrappers needed
  wrappersP = numP / wrapperCapacityP
  wrappersN = numN / wrapperCapacityN
  wrappersD = numD / wrapperCapacityD
  wrappersQ = numQ / wrapperCapacityQ

  # Determine value of currency
  valueP = numP * valPerP
  valueN = numN * valPerN
  valueD = numD * valPerD
  valueQ = numQ * valPerQ
  valueTotal = valueP + valueN + valueD + valueQ