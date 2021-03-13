"""Count the number of vowels in a string.
By Ted Silbernagel
"""


def count_vowels(data: str) -> None:
  counts = {
      'A': 0,
      'E': 0,
      'I': 0,
      'O': 0,
      'U': 0,
  }

  for char in data.upper():
    if char in counts.keys():
      counts[char] += 1

  # Print counts for user
  for vowel, count in counts.items():
    if count:
      print(f'{vowel}: {count}')


if __name__ == '__main__':
  print('This program will count the number of vowels in a word/string.')
  data = input('Please enter a string: ')
  count_vowels(data)
