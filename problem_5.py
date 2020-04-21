from lib import prime
from collections import defaultdict
from functools import reduce
from operator import mul

def least_common_multiple(ns):
  merged = defaultdict(int)

  for n in ns:
    prime_factors = prime.prime_factors(n)
    for factor, count in prime_factors.items():
      existing_count = merged[factor]
      new_count = max(existing_count, count)
      merged[factor] = new_count
  
  lcm = reduce(mul, (n**c for (n, c) in merged.items()))
  return lcm

print(least_common_multiple(range(1,20)))