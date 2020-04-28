from itertools import islice

def decimal_expansion(d):
  'Compute the decimal expansion of 1/d'
  n = 1
  while True:
    digit, remainder = divmod(10*n, d)
    yield (digit, remainder)
    n = remainder

def recurring_cycle_length(d):
  seen_remainders = []
  decimal_expansion_iter = decimal_expansion(d)
  while True:
    (digit, remainder) = next(decimal_expansion_iter)
    if remainder == 0:
      return 0
    elif remainder in seen_remainders:
      # we have entered a cycle
      cycle_length = seen_remainders.index(remainder) + 1
      return cycle_length
    else:
      seen_remainders.insert(0, remainder)

max_cycle_length = 0
best_value = None
for d in range(1, 1000):
  cycle_length = recurring_cycle_length(d)
  if cycle_length >= max_cycle_length:
    max_cycle_length = cycle_length
    best_value = d

print(best_value)
print(max_cycle_length)