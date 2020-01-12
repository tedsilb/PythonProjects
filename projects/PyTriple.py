# Check to see if three sides form a pythagorian triple.
# By Ted Silbernagel
# https://en.wikipedia.org/wiki/Pythagorean_triple


# Define the function that will check for this
def py_triple(a, b, c):
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

  # Determine if the squared numbers form a pythagorean triple
  if largest_no ** 2 == (small_no1 ** 2 + small_no2 ** 2):
    return True
  else:
    return False

# Gather numbers from user
print('Please enter three whole numbers. '
      'This function will check to see if they form a pythagorean triple.')
nums = [
  int(input('Please enter your first number: ')),
  int(input('Please enter your second number: ')),
  int(input('Please enter your third number: ')),
]

# Call the function, print response
if py_triple(nums[0], nums[1], nums[2]):
  print('Yes, this is a pythagorean triple.')
else:
  print('No, this is not a pythagorean triple.')
