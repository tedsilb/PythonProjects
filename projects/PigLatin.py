"""This program will convert a word or sentence to pig latin.
By Ted Silbernagel
"""

import string


def convert_pig_latin(input_string):
  # Make translator object to strip punctuation
  translator = str.maketrans('', '', string.punctuation)

  # Strip punctuation, lowercase, split into list of words
  input_list = input_string.translate(translator).lower().split(' ')

  # Set up lists for reference
  pig_latin_list = []
  vowels = ['a', 'e', 'i', 'o', 'u']
  consonant_clusters = [
      'bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
      'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw',
      'wh', 'wr'
  ]

  # Convert each word to pig latin
  for word in input_list:
    if word[0:2] in consonant_clusters:
      pig_latin_list.append(word[2:] + word[0:2] + 'ay')
    elif word[0:1] in vowels:
      pig_latin_list.append(word + 'way')
    else:
      pig_latin_list.append(word[1:] + word[0:1] + 'ay')

  # Turn list back into string, return
  return ' '.join(pig_latin_list)


# Gather data from user, call function
print('This program will convert a word or string to Pig Latin')
print(convert_pig_latin(input('Please enter a word or sentence: ')))
