# Check to see if three sides form a pythatgorian triple.
# By Ted Silbernagel
# https://en.wikipedia.org/wiki/Pythagorean_triple


# Define the function that will check for this
def pyTriple(a, b, c):
  # Figure out which side is the longest
  if (a > b) and (a > c):
    largestNo = a
    smallNo1 = b
    smallNo2 = c
  elif (b > a) and (b > c):
    largestNo = b
    smallNo1 = a
    smallNo2 = c
  elif (c > a) and (c > b):
    largestNo = c
    smallNo1 = a
    smallNo2 = b

  # Square the numbers
  lNoSq = largestNo * largestNo
  sNo1Sq = smallNo1 * smallNo1
  sNo2Sq = smallNo2 * smallNo2

  # Determine if the numbers form a pythagorean triple
  if lNoSq == (sNo1Sq + sNo2Sq):
    return True
  return False

# Gather numbers from user
print('Please enter three whole numbers. This function will check to see if they form a pythagorean triple.')
nums = [
  int(input('Please enter your first number: ')),
  int(input('Please enter your second number: ')),
  int(input('Please enter your third number: ')),
]

# Call the function, print response
if pyTriple(nums[0], nums[1], nums[2]):
  print('Yes, this is a pythagorean triple.')
else:
  print('No, this is not a pythagorean triple.')
