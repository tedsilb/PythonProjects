"""Generate a multiplication table.
By Ted Silbernagel
"""


def gen_multi_table(to_gen: int) -> None:
  # Add one to toGen
  to_gen += 1

  # Print the headers
  current_row = '     '
  for number in range(1, to_gen):
    if number < 10:
      current_row += f'   {number} '
    else:
      current_row += f'  {number} '

  print(current_row)

  # Print rows
  for number in range(1, to_gen):
    # Initialise first number
    if number < 10:
      current_row = f'   {number} '
    else:
      current_row = f'  {number} '

    # Start multiplications
    for multi_num in range(1, to_gen):
      if (multi_num * number) < 10:
        current_row += f'   {multi_num * number} '
      elif (multi_num * number) < 100:
        current_row += f'  {multi_num * number} '
      else:
        current_row += f' {multi_num * number} '

    print(current_row)


# Gather the number of rows/columns to generate
print('This program will generate a multiplication table (up to 31, cleanly).')
user_no = int(input('Please enter the number of rows/columns to generate: '))
print('\n')

# Run function
gen_multi_table(user_no)
