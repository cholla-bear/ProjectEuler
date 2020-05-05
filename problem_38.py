from math import ceil
from functools import reduce
from operator import concat

numerals = set([str(i) for i in range(1,10)])

def is_pandigital(n):
  digits = str(n)
  return len(digits) == 9 and set(digits) == numerals

max_prod = 0

for n in range(2,10):
  max_num_digits = ceil(9/n)
  upper_bound = 10**max_num_digits
  for k in range(1, upper_bound):
    prod = [k*i for i in range(1,n+1)]
    prod_concat = int(reduce(concat, [str(x) for x in prod]))
    if is_pandigital(prod_concat):
      max_prod = max(prod_concat, max_prod)

print(max_prod)