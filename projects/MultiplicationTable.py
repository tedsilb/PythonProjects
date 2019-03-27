# Generate a multiplication table.
# By Ted Silbernagel

# Define function
def genMultiTable(toGen):
  # Add one to toGen
  toGen += 1

  # Print the headers
  currentRow = '     '
  for number in range(1, toGen):
    if number < 10:
      currentRow += f'   {number} '
    else:
      currentRow += f'  {number} '
  print(currentRow)

  # Print rows
  for number in range(1, toGen):
    # Initialise first number
    if number < 10:
      currentRow = f'   {number} '
    else:
      currentRow = f'  {number} '
    # Start multiplications
    for multiNum in range(1, toGen):
      if (multiNum * number) < 10:
        currentRow += f'   {multiNum * number} '
      elif (multiNum * number < 100):
        currentRow += f'  {multiNum * number} '
      else:
        currentRow += f' {multiNum * number} '
    print(currentRow)

# Gather the number of rows/columns to generate
print('This program will generate a multiplication table (up to 31, cleanly).')
userNo = int(input('Please enter the number of rows/columns to generate: '))
print('\n')

# Run function
genMultiTable(userNo)
