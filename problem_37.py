from lib.prime import is_prime, primes
from operator import concat
from functools import reduce

def truncatable_primes_brutal():
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

def truncatable_primes():

  one_digit_primes = [2,3,5,7]
  odd_digits = [1,3,5,7,9]

  def extend_truncatable(p):
    extended_primes = list(filter(is_prime, [10*p + digit for digit in odd_digits]))
    return list(filter(is_truncatable, extended_primes)) + reduce(concat, [extend_truncatable(p) for p in extended_primes], [])

  return reduce(concat, [extend_truncatable(p) for p in one_digit_primes], [])

trunc = truncatable_primes()
print(trunc)
print(sum(trunc))