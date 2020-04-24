from lib import prime

def is_abundant(n):
  divisors = prime.proper_divisors(n)
  return sum(divisors) > n

abundant_nums = list(filter(is_abundant, range(2,28123)))

