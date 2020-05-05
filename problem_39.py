from math import sqrt, ceil
from lib.prime import relatively_prime
from collections import defaultdict

perimeter_limit = 1000

def enumerate_triples(perimeter_limit):
  triples = []
  upper_bound_long = ceil(perimeter_limit/2) + 1
  upper_bound_short = ceil(perimeter_limit/(2 + sqrt(2))) + 1
  for a in range(1, upper_bound_short):
    for b in range(a, upper_bound_long):
      c = sqrt(a**2 + b**2)
      if c.is_integer() and (a + b + c) <= perimeter_limit:
        triples.append((a, b, int(c)))
  return triples

perimeters = defaultdict(int)

for triple in enumerate_triples(perimeter_limit):
  p = sum(triple)
  perimeters[p] += 1

sorted_perimeters = sorted(perimeters.items(), key = lambda x: x[1])
most_common_perimeter = sorted_perimeters[-1][0]

print(most_common_perimeter)