"""99 bottles lyrics generator.
By Ted Silbernagel
"""

if __name__ == '__main__':
  # Start at 99 and work backwards
  for i in range(99, 0, -1):
    if i == 2:
      print('2 bottles of beer on the wall, 2 bottles of beer!')
      print('Take one down, pass it around, 1 bottle of beer on the wall!')
    elif i == 1:
      print('1 bottle of beer on the wall, 1 bottle of beer!')
      print('Take it down, pass it around, '
            'no more bottles of beer on the wall!')
    else:
      print(f'{i} bottles of beer on the wall, {i} bottles of beer!')
      print('Take one down, pass it around, '
            f'{i - 1} bottles of beer on the wall!')
