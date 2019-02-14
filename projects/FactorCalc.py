# Calculates all factors of a number

# Define function
def calcFactors():
  # Get number from user
  print('This program will calculate all factors of the number you specify.')
  userNo = int(input('Please enter a number: '))
  
  # Create array to store the factors in
  allFactors = []

  # Calculate factors
  for number in range(1, userNo + 1):
    if (userNo % number) == 0:
      allFactors.append(number)
  
  # Return data to user
  print(f'All factors of {userNo}: {allFactors}')

# Call function
calcFactors()