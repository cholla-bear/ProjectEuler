from itertools import takewhile, count
from collections import defaultdict

def triangle(n):
  return n*(n + 1)//2

def square(n):
  return n**2

def pentagon(n):
  return n*(3*n - 1)//2

def hexagon(n):
  return n*(2*n - 1)

def heptagon(n):
  return n*(5*n - 3)//2

def octagon(n):
  return n*(3*n - 2)

def take_4digit(func):
  return filter(
    lambda x: x >= 1000,
    takewhile(
      lambda x: x < 10000,
      map(
        func,
        count(),
  )))

def build_prefix_dict(func):
  prefix_dict = defaultdict(list)
  values = take_4digit(func)
  for n in values:
    prefix = n // 100
    prefix_dict[prefix] += [n]
  return prefix_dict

prefix_dicts = list(map(build_prefix_dict, [triangle, square, pentagon, hexagon, heptagon]))

def extend_cycle(cycle, used_types):
  suffix = cycle[-1] % 100
  prefix = cycle[0] // 100
  if len(cycle) == 6 and suffix == prefix:
    print(f"Found solution: {cycle} sum={sum(cycle)}")
    return
  available_types = set(range(5)).difference(used_types)
  for i in available_types:
    prefix_dict = prefix_dicts[i]
    for match in prefix_dict[suffix]:
      extend_cycle(cycle + [match], used_types.union({i}))

for n in take_4digit(octagon):
  extend_cycle([n], set())