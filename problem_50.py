from lib.prime import sieve
import numpy as np

max_prime = 10**6

primes = sieve(max_prime)
prime_set = set(primes)
n = len(primes)

# This array will accumulate the sum of sequential
# primes starting at the corresponding index
prime_sums = primes

longest_prime_sum = 0

for i in range(1, n):
  # Elements of prime_sums contain the sum of sequential
  # primes (i+1) terms long starting with the corresponding
  # element of the primes array
  prime_sums = prime_sums[:n-i] + primes[i:]
  for x in prime_sums[prime_sums < max_prime]:
    if x in prime_set:
      longest_prime_sum = x
    

print(longest_prime_sum)