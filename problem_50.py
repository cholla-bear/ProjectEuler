from lib.prime import sieve
import numpy as np

max_prime = 10**6

primes = sieve(max_prime)
prime_set = set(primes)
n = len(primes)

prime_sums = primes

longest_prime_sum = 0

for i in range(1, n):
  prime_sums = prime_sums[:n-i] + primes[i:]
  for x in prime_sums[prime_sums < max_prime]:
    if x in prime_set:
      longest_prime_sum = x

print(longest_prime_sum)