# from lib import prime
# import numpy as np

# def is_abundant(n):
#   divisors = prime.proper_divisors(n)
#   return sum(divisors) > n

# abundant_nums = list(filter(is_abundant, range(2,28123)))

# sum_abundant = np.zeros(28124, dtype=bool)

# for i, a1 in enumerate(abundant_nums):
#   for j in range(i, len(abundant_nums)):
#     a2 = abundant_nums[j]
#     if a1 + a2 < sum_abundant.shape[0]:
#       sum_abundant[a1 + a2] = True


# s = 0
# for n, is_sum in enumerate(sum_abundant):
#   if not is_sum:
#     s += n

# print(s)