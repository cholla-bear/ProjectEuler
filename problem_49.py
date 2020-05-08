from itertools import permutations, combinations
from collections import defaultdict
from functools import reduce
from operator import concat
from lib.digits import digits_to_num

def find_arithmetic_subsequences(seq):
  for i, n1 in enumerate(seq):
    for n2 in seq

def test_permutations(digits):
  permuted_digits = permutations(digits)
  vals = [digits_to_num(p) for p in permuted_digits]
  subseqs = find_arithmetic_subsequences(vals)
  print(subseqs)

def increasing_prime_permutations(n_digits):
  pass

test_permutations([1, 4, 8, 7])