from math import sqrt
from itertools import count

def is_triangular(x):
  # From the quadratic formula
  n = (-1 + sqrt(1 + 8*x))/2
  return n.is_integer()

def is_pentagonal(x):
  # From the quadratic formula:
  n = (1 + sqrt(1 + 24*x))/6
  return n.is_integer()

def hexagonal(n):
  return n*(2*n - 1)

def get_next_tri_pent_hex(n_start):
  for n in count(n_start):
    x = hexagonal(n)
    if is_triangular(x) and is_pentagonal(x):
      return x

print(get_next_tri_pent_hex(286))