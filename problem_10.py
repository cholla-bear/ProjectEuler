from lib import prime
from itertools import takewhile, islice
from functools import reduce

n = 2000000
result = sum(takewhile(lambda x: x<n, prime.primes()))
print(result)