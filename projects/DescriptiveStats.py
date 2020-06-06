"""Calculate descriptive statistics for a list of numbers.
By Ted Silbernagel
"""

from typing import Dict, List, Union


def gather_numbers() -> List[float]:
  # Prepare to gather numbers
  numbers_list = []

  # Gather list of numbers from user
  while True:
    entered_number = input('Please enter a number (press enter to stop): ')
    if entered_number == '':
      break
    else:
      numbers_list.append(float(entered_number))

  return numbers_list


def calc_mean(data: List[float]) -> float:
  return sum(data) / len(data)


def calc_median(data: List[float]) -> Union[float, List[float]]:
  sorted_data = sorted(data)

  # If the list is even length, grab the middle two numbers
  if not len(sorted_data) % 2:
    return [
        sorted_data[int((len(sorted_data) / 2) - 1)],
        sorted_data[int(len(sorted_data) / 2)],
    ]

  # If list is odd length, grab the middle number
  else:
    return sorted_data[len(sorted_data) // 2]


def calc_mode(data: List[float]) -> float:
  sorted_data = sorted(data)
  return max(set(sorted_data), key=sorted_data.count)


def calc_variance(data: List[float]) -> float:
  mean = calc_mean(data)
  return sum([((num - mean)**2) for num in data]) / len(data)


def descriptive_stats(numbers_list: List[float]) -> Dict[str, float]:
  # Round based on user input
  round_to = int(
      input('How many decimal places would you like your numbers '
            'rounded to? '))

  # Set up return data dict
  return_data = {
      'mean': round(calc_mean(numbers_list), round_to),
      'median': calc_median(numbers_list),
      'mode': calc_mode(numbers_list),
      'min': min(numbers_list),
      'max': max(numbers_list),
      'variance': round(calc_variance(numbers_list), round_to),
  }

  return_data['stDev'] = round(return_data['variance']**0.5, round_to)
  return_data['stErr'] = round(return_data['stDev'] / len(numbers_list),
                               round_to)

  # Ask user for confidence interval
  return_data['confInt'] = int(
      input('Please enter a confidence interval (90, 95, 99): '))
  t_stats = {
      90: 1.64,
      95: 1.96,
      99: 2.58,
  }

  # Calculate confidence interval
  return_data.update({
      'lowerBound':
          round(
              return_data['mean'] -
              (t_stats[return_data['confInt']] * return_data['stErr']),
              round_to),
      'upperBound':
          round(
              return_data['mean'] +
              (t_stats[return_data['confInt']] * return_data['stErr']),
              round_to),
  })

  return return_data


# Call function to gather numbers and calculate descriptive stats
response = descriptive_stats(gather_numbers())

# Print data for user
print(f'Mean:     {response["mean"]}')
print(f'Median:   {response["median"]}')
print(f'Mode:     {response["mode"]}')
print(f'Range:    [{response["min"]}, {response["max"]}]')
print(f'Variance: {response["variance"]}')
print(f'Standard Deviation: {response["stDev"]}')
print(f'Standard Error:     {response["stErr"]}')
print(f'{response["confInt"]}% confidence interval:')
print(f'  Lower Bound: {response["lowerBound"]}')
print(f'  Upper Bound: {response["upperBound"]}')
