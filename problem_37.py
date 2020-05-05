from lib.prime import is_prime, primes

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

  def extend_truncatable(p, truncatable):
    for digit in odd_digits:
      trial_p = 10*p + digit
      if is_prime(trial_p):
        if is_truncatable(trial_p):
          truncatable.append(trial_p)
        extend_truncatable(trial_p, truncatable)
  
  truncatable = []
  for p in one_digit_primes:
    extend_truncatable(p, truncatable)
  return truncatable

trunc = truncatable_primes()
print(trunc)
print(sum(trunc))