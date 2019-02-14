# Generate a multiplication table.

# Define function
def genMultiTable():
  # Gather the number of rows/columns to generate
  print('This program will generate a multiplication table (up to 31, cleanly).')
  toGen = int(input('Please enter the number of rows/columns to generate: '))
  toGen += 1
  print('\n')

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

# Run function
genMultiTable()