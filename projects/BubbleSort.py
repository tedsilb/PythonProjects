# Super basic bubble sort algorithm
# By Ted Silbernagel


# Define function to check to see if a list is sorted
def listIsSorted(listToCheck):
  for item in listToCheck:
    itemIndex = listToCheck.index(item)
    if itemIndex != len(listToCheck) - 1:
      nextItemIndex = itemIndex + 1
      nextItem = listToCheck[nextItemIndex]
      if nextItem < item:
        return False
  return True


# Define function to bubble sort
def bubbleSort(userList):
  # First parse the numbers
  listToSort = [float(item) for item in userList.split(',')]

  # Then get down to business
  while not listIsSorted(listToSort):
    for item in listToSort:
      itemIndex = listToSort.index(item)
      # If not the last item in the list
      if itemIndex != len(listToSort) - 1:
        # Get the indexes
        nextItemIndex = itemIndex + 1
        nextItem = listToSort[nextItemIndex]
        # If out of order,
        if item > nextItem:
          # Switch them
          listToSort[itemIndex], listToSort[nextItemIndex] = listToSort[nextItemIndex], listToSort[itemIndex]
      else:
        pass
  return listToSort

# Get data from user, call function
print('This program will bubble sort a given list of numbers.')
inputList = input('Please enter some numbers, separated by commas, to be sorted: ')
print(bubbleSort(inputList))
