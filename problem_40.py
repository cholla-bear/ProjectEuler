from operator import mul
from functools import reduce
from itertools import count, islice, takewhile

max_order = 6

def solve_by_string():
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


def solve_by_generator():
  def champ_gen():
    for i in count(1):
      for digit in str(i):
        yield int(digit)

  desired_indices = [10**n - 1 for n in range(max_order + 1)]
  champ_digits = islice(champ_gen(), 10**max_order)
  filtered_digits = filter(lambda x: x[0] in desired_indices, enumerate(champ_digits))
  prod = reduce(mul, (x[1] for x in filtered_digits))
  print(prod)

def champ_digit(n):
  def digits_up_to_order(j):
    return sum([9*(i+1)*10**i for i in range(j)])
  order = 1
  while digits_up_to_order(order) < n:
    order += 1
  index_within_order = n - digits_up_to_order(order - 1)
  sequence_num, remainder = divmod(index_within_order, order)
  integer = sequence_num + 10**(order - 1)
  digit = int(str(integer)[remainder])
  return digit

print(reduce(mul, [champ_digit(n-1) for n in [10**j for j in range(max_order + 1)]]))
