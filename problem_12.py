from lib import prime
from collections import Counter
from functools import reduce
from operator import mul

def tri(n):
  return n*(n+1)/2

def num_factors_tri(n):
  '''Return the number of factors in the nth triangle number'''

  # Since tri(n) = n(n+1)/2 we start with the factors of n and n+1
  f1 = prime.prime_factors(n)
  f2 = prime.prime_factors(n+1)
  merged_factors = Counter(f1) + Counter(f2)

  # Remove a factor of 2 to cancel with denominator
  merged_factors[2] -= 1

  # Each prime factor can contribute 0 to n times in the final
  # product (where n is the merged count of that prime factor)
  return reduce(mul, (v + 1 for v in merged_factors.values()), 1)


# Find the smallest triangle number with more than 500 factors
n = 1
while(num_factors_tri(n) <= 500):
  n += 1
print(tri(n))
print(n)