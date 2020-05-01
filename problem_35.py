from lib.prime import primes, is_prime
from itertools import takewhile

def digit_rotations(n):
  s = str(n)
  for i in range(len(s)):
    yield int(s[i:] + s[:i])

def all_rotations_prime(p):
  return all(map(is_prime, digit_rotations(p)))

def circular_primes(limit):
  primes_to_limit = takewhile(lambda x: x < limit, primes())
  return filter(all_rotations_prime, primes_to_limit)

limit = 1000000
print(len(list(circular_primes(limit))))