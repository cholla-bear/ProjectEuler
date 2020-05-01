import itertools
from math import factorial
from functools import lru_cache

factorials = [factorial(n) for n in range(10)]

def max_num_digits():
  '''Find an upper bound for the number of digits'''
  for num_digits in itertools.count(2):
    if 10**(num_digits - 1) > num_digits * factorial(9):
      # A number of this length cannot satisfy the criterion.
      # The smallest n-digit number is bigger than the
      # biggest possible sum(factorial(digit))
      return num_digits - 1

def upper_bound():
  return max_num_digits()*factorial(9)

@lru_cache(maxsize=None)
def sum_of_factorials(digits):
  return sum([factorials[d] for d in digits])

def factorial_of_digits():
  expressible = []
  for n in range(3, upper_bound()):
    digits = [int(d) for d in str(n)]
    sum_facts = sum_of_factorials(tuple(sorted(digits)))
    if n == sum_facts:
      expressible.append(n)
  return expressible

print(sum(factorial_of_digits()))