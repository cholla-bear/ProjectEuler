from math import sqrt
from itertools import count

def is_pentagonal(p):
  # From the quadratic formula:
  n = (1 + sqrt(1 + 24*p))/6
  return n.is_integer()

def pent(n):
  return int(n*(3*n - 1)/2)

def smallest_diff():
  upper_i = None
  smallest_d = None
  for i in count(1):
    if upper_i and i > upper_i:
      break
    for j in range(i - 1, 0, -1):
      diff = pent(i) - pent(j)
      if smallest_d and diff > smallest_d:
        break
      add = pent(i) + pent(j)
      if not is_pentagonal(diff) or not is_pentagonal(add):
        continue
      print("found solution: i={} j={} diff={}".format(i, j, diff))
      smallest_d = min(diff, smallest_d) if smallest_d else diff
      # find the largest index such that pent(i) - pent(i+1) > smallest_d
      upper_i = int((smallest_d-1)/3) + 1
      print("upper_i={}".format(upper_i))
  return smallest_d

print(smallest_diff())