from lib.prime import primes, is_prime
from itertools import takewhile
import itertools
from functools import reduce
from operator import concat

def is_pandigital(n):
  n_str = str(n)
  num_digits = len(n_str)
  if num_digits > 9:
    return False
  return set(n_str) == set([str(i) for i in range(1, num_digits + 1)])

def solve_brutal():
  # Too slow
  upper_bound = 987654321
  pandigital_primes = list(filter(is_pandigital, takewhile(lambda x: x <= upper_bound, primes())))
  print(pandigital_primes[-1])

def solve_with_permutations():
  # Go through all possible pandigital numbers from largest to smallest
  for num_digits in range(9,0,-1):
    digits = [str(i) for i in range(num_digits, 0, -1)]
    permutations = itertools.permutations(digits)
    for permutation in permutations:
      n = int(reduce(concat, permutation))
      if is_prime(n):
        return n

print(solve_with_permutations())