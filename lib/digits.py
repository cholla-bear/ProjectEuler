from collections import defaultdict

def digits_to_num(digits):
  '''Accepts digits as either numbers or strings'''
  return sum([int(d)*10**i for i, d in enumerate(reversed(digits))])

def num_to_digits(n):
  '''Return the digits of n as a list of integers'''
  return [int(d) for d in str(n)]

def digit_counts(n):
  digit_counts = defaultdict(int)
  for d in num_to_digits(n):
    digit_counts[d] += 1
  return dict(digit_counts)

def digit_indexes(n):
  digit_indexes = defaultdict(list)
  for i, digit in enumerate(num_to_digits(n)):
    digit_indexes[digit].append(i)
  return dict(digit_indexes)