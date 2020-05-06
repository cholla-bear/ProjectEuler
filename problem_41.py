from lib.prime import primes
from itertools import takewhile

def is_pandigital(n):
  n_str = str(n)
  num_digits = len(n_str)
  if num_digits > 9:
    return False
  pandigital = set(n_str) == set([str(i) for i in range(1, num_digits + 1)])
  if pandigital:
    print(n)
  return pandigital

upper_bound = 987654321

pandigital_primes = list(filter(is_pandigital, takewhile(lambda x: x <= upper_bound, primes())))

print(pandigital_primes[-1])