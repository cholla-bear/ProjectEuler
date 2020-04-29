import itertools

def max_num_digits(power):
  '''Find an upper bound for the number of digits'''
  for num_digits in itertools.count(2):
    if 10**(num_digits - 1) > num_digits * 9**power:
      # A number of this length cannot satisfy the criterion.
      # The smallest n-digit number is bigger than the
      # biggest possible sum(digit**power)
      return num_digits - 1

def power_of_digits(power):
  expressible = []
  upper_bound = max_num_digits(power) * 9**power
  for n in range(2, upper_bound):
    digits = [int(d) for d in str(n)]
    sum_of_powers = sum([d**power for d in digits])
    if n == sum_of_powers:
      expressible.append(n)
  return expressible

power = 5
nums = power_of_digits(power)
print(nums)
print(sum(nums))