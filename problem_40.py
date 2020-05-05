from operator import mul
from functools import reduce
from itertools import count, islice

def champ(n):
  '''Return at least n digits of the fractional part of the decimal
  Champernowe constant as a string'''
  res = ""
  i = 1
  while len(res) < n:
    res += str(i)
    i += 1
  return res

max_order = 6

champ_str = champ(10**max_order)

prod = reduce(mul, ([int(champ_str[10**i - 1]) for i in range(max_order + 1)]))

print(prod)

def champ_gen():
  for i in count(1):
    for digit in str(i):
      yield int(digit)

desired_indices = [10**n - 1 for n in range(max_order + 1)]
champ_digits = islice(champ_gen(), 10**max_order)
filtered_digits = filter(lambda x: x[0] in desired_indices, enumerate(champ_digits))
prod = reduce(mul, (x[1] for x in filtered_digits))
print(prod)