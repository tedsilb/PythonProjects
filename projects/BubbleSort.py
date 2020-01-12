# Super basic bubble sort algorithm
# By Ted Silbernagel

from typing import List, Text


# Check if a list is sorted
def list_is_sorted(list_to_check: List[float]) -> bool:
  for item in list_to_check:
    item_index = list_to_check.index(item)
    if item_index != len(list_to_check) - 1:
      next_item_index = item_index + 1
      next_item = list_to_check[next_item_index]
      if next_item < item:
        return False
  return True


# Do the bubble sorting
def bubble_sort(user_list: Text) -> List[float]:
  # First parse the numbers
  list_to_sort = [float(item) for item in user_list.split(',')]

  # Then get down to business
  while not list_is_sorted(list_to_sort):
    for item in list_to_sort:
      item_index = list_to_sort.index(item)
      # If not the last item in the list
      if item_index != len(list_to_sort) - 1:
        # Get the indexes
        next_item_index = item_index + 1
        next_item = list_to_sort[next_item_index]
        # If out of order,
        if item > next_item:
          # Switch them
          (list_to_sort[item_index], list_to_sort[next_item_index]
          ) = (list_to_sort[next_item_index], list_to_sort[item_index])
      else:
        pass
  return list_to_sort

# Get data from user, call function
print('This program will bubble sort a given list of numbers.')
input_list = input('Please enter some numbers, '
                  'separated by commas, to be sorted: ')
print(bubble_sort(input_list))
