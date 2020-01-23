"""Collatz Conjecture
By Ted Silbernagel
Start with a number n > 1.
Find the number of steps it takes to reach one using the following process:
  If n is even, divide it by 2.
  If n is odd, multiply it by 3 and add 1.
"""


def collatz(user_no: int) -> None:
  current_no = user_no
  print(current_no)
  steps = 0

  while current_no != 1:
    if current_no % 2 == 0:
      current_no //= 2
    else:
      current_no = (current_no * 3) + 1
    steps += 1
    print(current_no)

  print(f'Took {steps} steps.')


# Call function
print('This program will perform the Collatz conjecture '
      'on a given whole number.')
collatz(int(input('Please enter a number: ')))
