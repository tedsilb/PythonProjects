# Goal 
#   Create a program that allows the user to input the total weight of each type of coin they have 
#   (pennies, nickels, dimes, and quarters), 
#   and then print out how many of each type of wrapper they would need, 
#   how many coins they have, and the estimated total value of all of their money.
#   Weight of each coin and how many fit inside each type of wrapper.
# Subgoals
#   Round all numbers printed out to the nearest whole number.
#   Allow the user to select whether they want to submit the weight in either grams or pounds.

def estimateWeight(pWgt, nWgt, dWgt, qWgt):
  # Parse arguments
  pWgt = float(pWgt)
  nWgt = float(nWgt)
  dWgt = float(dWgt)
  qWgt = float(qWgt)
  
  # Define weights 
  wgtPerPenny = 2.5
  wgtPerNickel = 5.0
  wgtPerDime = 2.268
  wgtPerQuarter = 2.67

  # Define amounts per wrapper
  wrapperCapacityP = 50
  wrapperCapacityN = 40
  wrapperCapacityD = 50
  wrapperCapacityQ = 40

  # Calculate number of coins for each weight
  pNum = pWgt / wgtPerPenny