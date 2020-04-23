from collections import defaultdict
from itertools import takewhile, islice
from math import sqrt
from functools import lru_cache

@lru_cache
def prime_factors(n):
  '''Returns a dictionary of prime factors with their counts'''
  prime_factors = defaultdict(int)

  while n % 2 == 0:
    prime_factors[2] += 1
    n = n/2

  trial_factor = 3

  while n > 1:
    q, r = divmod(n, trial_factor)
    if r == 0:
      n = q
      prime_factors[trial_factor] += 1
    else:
      trial_factor += 2

  return prime_factors

def take_primes(n):
  '''Returns a list of the first n primes'''
  return list(islice(primes(), n))

def primes():
  '''Return a generator of prime numbers'''
  known_primes = []
  test_num = 2
  while True:
    filtered_primes = takewhile(lambda x: x <= sqrt(test_num), known_primes)
    if not any(test_num % p == 0 for p in filtered_primes):
      known_primes.append(test_num)
      yield test_num
    test_num += 1

