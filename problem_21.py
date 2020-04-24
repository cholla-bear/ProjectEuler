from lib import prime
from functools import lru_cache

amicable_numbers = []

def sum_proper_divisors(n):
  return sum(prime.proper_divisors(n))

for n in range(2,10000):
  d1 = sum_proper_divisors(n)
  if d1 == n:
    continue # not technically amicable
  if d1 < n:
    continue # already checked this pair
  d2 = sum_proper_divisors(d1)
  if d2 == n:
    amicable_numbers += [n, d1]

print(sum(amicable_numbers))