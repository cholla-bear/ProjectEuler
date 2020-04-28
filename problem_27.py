from lib.prime import is_prime, primes
from itertools import takewhile, count

def longest_prime_sequence(a, b):
  def poly(n):
    return n**2 + a*n + b
  prime_seq = takewhile(is_prime, map(poly, count()))
  return len(list(prime_seq))

max_seq_len = 0
best_coeffs = None
for b in takewhile(lambda x: x < 1000, primes()):
  for a in range(-999, 1000):
    seq_len = longest_prime_sequence(a, b)
    if seq_len > max_seq_len:
      max_seq_len = seq_len
      best_coeffs = (a, b)

print(best_coeffs)
print(max_seq_len)
print("a*b = {}".format(best_coeffs[0]*best_coeffs[1]))