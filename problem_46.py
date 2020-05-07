from lib.prime import sieve, is_prime
import itertools
from math import sqrt

primes = sieve(10000)

def disprove_goldbach():
  def satisfies_goldbach(n):
    for p in primes[primes < n]:
      r = n - p
      if sqrt(r/2).is_integer():
        return True
    return False

  for n in itertools.count(9, 2):
    if is_prime(n):
      continue
    if not satisfies_goldbach(n):
      return n

print(disprove_goldbach())