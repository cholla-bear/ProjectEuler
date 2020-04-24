from lib import prime
import numpy as np

def is_abundant(n):
  divisors = prime.proper_divisors(n)
  return sum(divisors) > n

abundant_nums = list(filter(is_abundant, range(2,28123)))

sum_abundant = np.zeros(28123, dtype=bool)

for i, a1 in enumerate(abundant_nums):
  for j in range(i, len(abundant_nums)):
    a2 = abundant_nums[j]
    sum_abundant[a1 + a2] = True

print(sum_abundant[:30])