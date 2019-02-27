# This pgoram will convert a word or sentence to pig latin.
# By Ted Silbernagel

# Import dependencies
import string

# Define function
def convertPigLatin(inputString):
  # Make translator object to strip puncuation
  translator = str.maketrans('', '', string.punctuation)

  # Strip punctuation from string
  inputString = inputString.translate(translator)

  # Lowercase the entire string
  inputString = inputString.lower()

  # Split string into list, based on spaces. want to isolate individual words
  inputList = inputString.split(' ')

  # Set up lists for reference
  pigLatinList = []
  vowels = ['a', 'e', 'i', 'o', 'u']
  consonantClusters = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sc']
  consonantClusters += ['sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']

  # Convert each word to pig latin
  for word in inputList:
    if word[0:2] in consonantClusters:
      pigLatinList.append(word[2:] + word[0:2] + 'ay')
    elif word[0:1] in vowels:
      pigLatinList.append(word + 'way')
    else:
      pigLatinList.append(word[1:] + word[0:1] + 'ay')

  # Turn list back into string
  pigLatinString = ' '.join(pigLatinList)

  # Return string to user
  return pigLatinString

# Gather data from user, call function
print('This program will convert a word or string to Pig Latin')
userString = input('Please enter a word or sentence: ')
response = convertPigLatin(userString)
print(response)