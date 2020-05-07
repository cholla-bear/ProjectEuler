from math import sqrt
from itertools import count

def is_pentagonal(p):
  # From the quadratic formula:
  n = (1 + sqrt(1 + 24*p))/6
  return n.is_integer()

def pent(n):
  return int(n*(3*n - 1)/2)

def smallest_diff():
  smallest_d = None
  for i in count(1):
    if smallest_d and pent(i) - pent(i - 1) > smallest_d:
      # we're done, all future diffs greater than smallest_d
      return smallest_d
    for j in range(i - 1, 0, -1):
      diff = pent(i) - pent(j)
      if smallest_d and diff > smallest_d:
        # all further pairs with this value of i will have a
        # diff larger than smallest_d
        break
      add = pent(i) + pent(j)
      if not is_pentagonal(diff) or not is_pentagonal(add):
        continue
      print("found solution: i={} j={} diff={}".format(i, j, diff))
      smallest_d = min(diff, smallest_d) if smallest_d else diff
  return smallest_d

print(smallest_diff())