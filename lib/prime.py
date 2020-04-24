from collections import defaultdict
import itertools
from itertools import takewhile, islice
from math import sqrt
from functools import lru_cache, reduce
from operator import mul

@lru_cache(maxsize=None)
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

def proper_divisors(n):
  '''Return a list of divisors of n, including 1 but excluding n'''
  if n == 0:
    raise ValueError
  if n == 1:
    return [1]
  pf = prime_factors(n)
  raised_factors = []
  for factor, power in pf.items():
    raised_factors.append([factor**n for n in range(power+1)])
  factor_components = itertools.product(*raised_factors)
  proper_divisors = [reduce(mul, xs) for xs in factor_components]
  proper_divisors.remove(n)
  return proper_divisors

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
