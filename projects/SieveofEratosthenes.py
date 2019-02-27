# This program uses the Sieve of Eratosthenes algorithm to find all prime numbers up to a given number.
# By Ted Silbernagel

# Define function
def sieveE(userNo):
  numToGen = int(userNo)
  numbersList = list(range(1, numToGen + 1))
  for number in numbersList:
    if number > 1:
      numMult = number
      for numMult in range(2, int(numToGen / number)):
        try:
          numbersList.remove(number * numMult)
        except:
          pass
      numbersList
  return numbersList

# Gather number from user, run function
print('This program will find all primes up to a given number.')
enteredNo = input('Please enter a number: ')
response = sieveE(enteredNo)
print(response)