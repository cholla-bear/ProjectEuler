from lib.prime import is_prime, primes
from itertools import islice

def truncatable_primes():
  prime_gen = primes()
  for p in primes():
    if is_truncatable(p):
      yield p

def is_truncatable(p):
  p_str = str(p)
  if len(p_str) == 1:
    return False
  for length in range(1, len(p_str)):
    trunc_left = p_str[:length]
    trunc_right = p_str[-length:]
    if not (is_prime(int(trunc_left)) and is_prime(int(trunc_right))):
      return False
  return True

trunc_primes = list(islice(truncatable_primes(), 11))
print(trunc_primes)
print(sum(trunc_primes))