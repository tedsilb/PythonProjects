# A simple FizzBuzz program
# By Ted Silbernagel

# Define function
def fizzBuzz():
  for i in range(1, 101):
    if (i % 3) == 0 and (i % 5) == 0:
      print('FizzBuzz')
    if (i % 3) == 0:
      print('Fizz')
    if (i % 5) == 0:
      print('Buzz')
    else:
      print(i)

# Call function
fizzBuzz()
