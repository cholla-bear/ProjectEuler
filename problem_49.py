import itertools
from collections import defaultdict
from functools import reduce
from operator import concat
from lib.digits import digits_to_num
from lib.prime import is_prime

def find_arithmetic_subsequences(seq):
  found_sequences = []
  for i, n1 in enumerate(seq):
    for j, n2 in enumerate(seq[i+1:], i+1):
      diff = n2 - n1
      subseq = [n1, n2]
      last_n = n2
      for k, n in enumerate(seq[j+1:], j+1):
        if n - last_n == diff:
          subseq.append(n)
          last_n = n
      if len(subseq) > 2:
        found_sequences.append(subseq)
  return found_sequences

def test_permutations(digits):
  permuted_digits = itertools.permutations(digits)
  vals = sorted(set([digits_to_num(p) for p in permuted_digits]))
  subseqs = find_arithmetic_subsequences(vals)
  prime_subseqs = []
  for seq in subseqs:
    if all([is_prime(n) for n in seq]):
      prime_subseqs.append(seq)
  return prime_subseqs

def increasing_prime_permutations(n_digits):
  numerals = range(10)
  solution_sequences = []
  for digits in itertools.combinations_with_replacement(numerals, n_digits):
    solution_sequences += test_permutations(digits)
  return solution_sequences

print(increasing_prime_permutations(4))