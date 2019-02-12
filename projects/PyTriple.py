# Check to see if three sides form a pythatgorian triple.
# https://en.wikipedia.org/wiki/Pythagorean_triple

# Define the function that will check for this
def pyTriple(a, b, c):
  # Turn the passed arguments into numbers
  a = int(float(a))
  b = int(float(b))
  c = int(float(c))

  # Figure out which side is the longest
  if (a > b and a > c):
    largestNo = a
    smallNo1 = b
    smallNo2 = c
  elif (b > a and b > c):
    largestNo = b
    smallNo1 = a
    smallNo2 = c
  elif (c > a and c > b):
    largestNo = c
    smallNo1 = a
    smallNo2 = b

  # Square the numbers
  lNoSq = largestNo * largestNo
  sNo1Sq = smallNo1 * smallNo1
  sNo2Sq = smallNo2 * smallNo2

  # Determine if the numbers form a pythagorean triple
  if (lNoSq == sNo1Sq + sNo2Sq):
    return 'Yes, this is a pythagorean triple.'
  else:
    return 'No, this is not a pythagorean triple.'

# Gather numbers from user
print('Please enter three whole numbers. This function will check to see if they form a pythagorean triple.')
number1 = input('Please enter your first number:')
number2 = input('Please enter your second number:')
number3 = input('Please enter your third number:')

# Run the function, print response
response = pyTriple(number1, number2, number3)
print(response)