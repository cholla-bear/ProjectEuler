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


#############################
def reduce_by_factor(n, reduct):
    n_reduced = n
    reduct_count = 0
    n_div_reduct, n_mod_reduct = divmod(n_reduced, reduct)
    while n_mod_reduct == 0:
        reduct_count += 1
        n_reduced = n_div_reduct
        n_div_reduct, n_mod_reduct = divmod(n_reduced, reduct)

    return (n_reduced, reduct_count)


def prime_factors(n):
    factors = defaultdict(int)
    n_reduced, factor_count = reduce_by_factor(n, 2)
    if factor_count:
        factors[2] = factor_count
    n_reduced, factor_count = reduce_by_factor(n_reduced, 3)
    if factor_count:
        factors[3] = factor_count

    k = 1
    while n_reduced > 1:
        for test_factor in (6 * k - 1, 6 * k + 1):
            n_reduced, factor_count = reduce_by_factor(n_reduced, test_factor)
            if factor_count:
                factors[test_factor] = factor_count
        k += 1

    return factors


# XXX
primes_1000 = sieve_primes(num_primes=1000)


def prime_factors_cached(n):
    factors = dict()
    k = 1
    while n > 1:
        for p in primes_1000:
            n, factor_count = reduce_by_factor(n, p)
            if factor_count:
                factors[p] = factor_count
        k += 1

    return factors
