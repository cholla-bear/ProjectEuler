from lib.digits import digit_indexes
from lib.prime import primes
from itertools import combinations
from collections import defaultdict
import sys

def replace_characters(s, c, indexes):
  for i in indexes:
    s = s[:i] + c + s[i+1:]
  return s

def digit_masks(n):
  '''
  Generate masks of the form:
  1123 -> ['x123', '1x23', 'xx23', '11x3', '112x']
  '''
  n_str = str(n)
  masks = []
  for digit, indexes in digit_indexes(n).items():
    digit_count = len(indexes)
    for n in range(1, digit_count + 1):
      mask_indexes = combinations(indexes, n)
      for index_set in mask_indexes:
        masks.append(replace_characters(n_str, 'x', index_set))
  return masks


def prime_digit_replacements(target_count):
  seen_masks = defaultdict(list)
  for p in primes():
    masks = digit_masks(p)
    for m in masks:
      seen_masks[m].append(p)
      if len(seen_masks[m]) == target_count:
        return seen_masks[m]

print(prime_digit_replacements(8))