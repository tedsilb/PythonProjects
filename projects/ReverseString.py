"""A function to reverse a string.
By Ted Silbernagel
"""


def reverse_string(input_word: str) -> str:
  return_word = ''

  for _ in input_word:
    return_word += input_word[-1:]
    input_word = input_word[:-1]

  return return_word


# Get user string, run function, print results
print(reverse_string(input('Please enter a word/string to reverse: ')))
