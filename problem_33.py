from lib.prime import prime_factors
from functools import reduce
from operator import mul, concat

def reduce_correctly(n, d):
  if n == 0:
    return (0, 1)
  # Have to copy for the LRU cache
  n_factors = prime_factors(n).copy()
  d_factors = prime_factors(d).copy()
  for factor, n_count in n_factors.items():
    if factor in d_factors:
      d_count = d_factors[factor]
      cancel_count = min(n_count, d_count)
      n_factors[factor] -= cancel_count
      d_factors[factor] -= cancel_count
  reduced_n = reduce(mul, [f**c for f, c in n_factors.items()], 1)
  reduced_d = reduce(mul, [f**c for f, c in d_factors.items()], 1)
  return (reduced_n, reduced_d)

def reduce_daftly(n, d):
  n_digits = [int(x) for x in str(n)]
  d_digits = [int(x) for x in str(d)]
  for digit in n_digits:
    if digit in d_digits:
      n_digits.remove(digit)
      d_digits.remove(digit)
  reduced_n = int(reduce(concat, [str(x) for x in n_digits]))
  reduced_d = int(reduce(concat, [str(x) for x in d_digits]))
  return (reduced_n, reduced_d)

special_fractions = []

for d in range(10,100):
  for n in range(10,d):
    if d % 10 == 0 and n % 10 == 0:
      # "trivial" case
      continue
    daft = reduce_daftly(n, d)
    if daft == (n, d):
      # didn't do anything
      continue
    if daft[1] == 0:
      continue
    daft = reduce_correctly(*daft)
    correct = reduce_correctly(n, d)
    if correct == daft:
      print("{} {} {}".format((n,d), correct, daft))
      special_fractions.append(correct)

n_prod = reduce(mul, [item[0] for item in special_fractions])
d_prod = reduce(mul, [item[1] for item in special_fractions])

print(reduce_correctly(n_prod, d_prod)[1])