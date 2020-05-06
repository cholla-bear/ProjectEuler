from collections import defaultdict
import itertools
from itertools import takewhile, islice
from math import sqrt
from functools import lru_cache, reduce
from operator import mul
import numpy as np

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
  yield 2
  test_num = 3
  while True:
    limit = sqrt(test_num)
    filtered_primes = takewhile(lambda x: x <= limit, known_primes)
    if not any(test_num % p == 0 for p in filtered_primes):
      known_primes.append(test_num)
      yield test_num
    test_num += 2

@lru_cache(maxsize=None)
def is_prime(n):
  if n <= 1:
    return False
  elif n == 2:
    return True
  elif n % 2 == 0:
    return False
  else:
    for trial_divisor in range(3, int(sqrt(n)) + 1, 2):
      if n % trial_divisor == 0:
        return False
  return True

def relatively_prime(a, b):
  prime_factors_a = prime_factors(a)
  prime_factors_b = prime_factors(b)
  return set(prime_factors_a).isdisjoint(set(prime_factors_b))

def sieve(n):
  # Help from here: 
  # https://stackoverflow.com/questions/49936222/an-efficient-sieve-of-eratosthenes-in-python
  flags = np.ones(n, dtype=bool)
  flags[0] = flags[1] = False
  for i in range(2, int(sqrt(n)) + 1):
    if flags[i]:
      flags[i*i::i] = False
  return np.flatnonzero(flags)