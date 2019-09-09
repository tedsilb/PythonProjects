# Collatz Conjecture
# By Ted Silbernagel
# Start with a number n > 1.
# Find the number of steps it takes to reach one using the following process:
#   If n is even, divide it by 2.
#   If n is odd, multiply it by 3 and add 1.


# Define function
def collatz(userNo):
  currentNo = userNo
  print(currentNo)
  steps = 0
  while currentNo != 1:
    if currentNo % 2 == 0:
      currentNo = int(currentNo / 2)
    else:
      currentNo = int(currentNo * 3) + 1
    steps += 1
    print(currentNo)
  print(f'Took {steps} steps.')

# Call function
print('This program will perform the Collatz conjecture on a given whole number.')
collatz(int(input('Please enter a number: ')))
