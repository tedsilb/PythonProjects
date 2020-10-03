"""Check to see if three sides form a Pythagorean triple.
By Ted Silbernagel
https://en.wikipedia.org/wiki/Pythagorean_triple
"""


def py_triple(a: int, b: int, c: int) -> bool:
  # Figure out which side is the longest
  if (a > b) and (a > c):
    largest_no = a
    small_no1 = b
    small_no2 = c
  elif (b > a) and (b > c):
    largest_no = b
    small_no1 = a
    small_no2 = c
  elif (c > a) and (c > b):
    largest_no = c
    small_no1 = a
    small_no2 = b
  else:
    raise Exception(f'Incorrect input: {a} {b} {c}')

  return largest_no**2 == (small_no1**2 + small_no2**2)


if __name__ == '__main__':
  print('Please enter three whole numbers. '
        'This function will check to see if they form a pythagorean triple.')
  nums = [
      int(input('Please enter your first number: ')),
      int(input('Please enter your second number: ')),
      int(input('Please enter your third number: ')),
  ]

  if py_triple(nums[0], nums[1], nums[2]):
    print('Yes, this is a pythagorean triple.')
  else:
    print('No, this is not a pythagorean triple.')
