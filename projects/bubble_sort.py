"""Super basic bubble sort algorithm.
By Ted Silbernagel
"""

from typing import List


def _parse_to_floats(user_nums: str) -> List[float]:
  return [float(item) for item in user_nums.split(',')]


def is_sorted(numbers: List[float]) -> bool:
  """Check if the list is sorted."""
  for item in numbers:
    item_index = numbers.index(item)
    if item_index != len(numbers) - 1:
      next_item_index = item_index + 1
      next_item = numbers[next_item_index]
      if next_item < item:
        return False

  return True


def bubble_sort(nums_to_sort: List[float]) -> List[float]:
  """Sort a list of floats using bubble sort."""
  while not is_sorted(nums_to_sort):
    for item in nums_to_sort:
      item_index = nums_to_sort.index(item)
      # If not the last item in the list
      if item_index != len(nums_to_sort) - 1:
        # Get the indexes
        next_item_index = item_index + 1
        next_item = nums_to_sort[next_item_index]
        # If out of order,
        if item > next_item:
          # Switch them
          (nums_to_sort[item_index],
           nums_to_sort[next_item_index]) = (nums_to_sort[next_item_index],
                                             nums_to_sort[item_index])

  return nums_to_sort


if __name__ == '__main__':
  print('This program will bubble sort a given list of numbers.')
  user_data = _parse_to_floats(
      input('Please enter some numbers, separated by commas, '
            'to be sorted: '))

  response = bubble_sort(user_data)
  print(response)
