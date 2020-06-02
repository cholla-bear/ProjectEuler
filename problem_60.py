from lib.prime import sieve
import networkx as nx
from itertools import combinations, product
from sympy.ntheory.primetest import isprime

max_prime = 10**5
target_n = 5

primes = sieve(max_prime)

def is_concat_prime(n1, n2):
  return isprime(int(f"{n1}{n2}")) and isprime(int(f"{n2}{n1}"))

def solve_with_graph():
  G = nx.Graph()
  min_sum = None

  for i, p1 in enumerate(primes[1:], 1):
    # Keep going until no further sums can be smaller than min_sum
    if min_sum and p1 > min_sum:
      return min_sum

    # Populate graph with primes that concatenate with p1
    edges_added = 0
    for p2 in primes[:i]:
      if is_concat_prime(p1, p2):
        G.add_edge(p1, p2)
        edges_added += 1

    # Hunt for a clique of size target_n
    if edges_added >= target_n - 1:
      neighbors = nx.neighbors(G, p1)
      for candidates in combinations(neighbors, target_n - 1):
        edges = [G.has_edge(*e) for e in combinations(candidates, 2)]
        if all(edges):
          solution = list(candidates) + [p1]
          print(f"Found candidate solution: {solution} sum={sum(solution)}")
          min_sum = min(min_sum, sum(solution)) if min_sum else sum(solution)

print(f"Best solution: {solve_with_graph()}")