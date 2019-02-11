# 99 bottles lyrics generator

def gen_lyrics():
  for i in range(99, 0, -1):
    if (i == 1):
      print(f'{i} bottle of beer on the wall, {i} bottle of beer!')
      print('Take it down, pass it around, no bottles of beer on the wall!')
    else:
      print(f'{i} bottles of beer on the wall, {i} bottles of beer!')
      print(f'Take one down, pass it around, {i - 1} bottles of beer on the wall!')

gen_lyrics()