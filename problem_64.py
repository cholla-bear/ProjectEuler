from math import floor, sqrt

def iteration_step(N, b1, c1):
  c2 = (N - b1**2)//c1
  a2 = floor(c1/(sqrt(N) + b1))
  b2 = -(b1 + a2*c2)
  return (a2, b2, c2)

def continued_fraction_sqrt(N):
  a0 = floor(sqrt(N))
  b = -a0
  c = 1
  seen_params = set()
  a_values = []
  while (b, c) not in seen_params:
    seen_params.add((b, c))
    (a, b, c) = iteration_step(N, b, c)
    a_values.append(a)
  return (a0, a_values)

def count_odd_periods(N_max):
  count = 0
  for N in range(2, N_max + 1):
    if sqrt(N).is_integer():
      continue
    (a0, a_values) = continued_fraction_sqrt(N)
    period = len(a_values)
    if period % 2 == 1:
      count += 1
  return count

print(count_odd_periods(10000))