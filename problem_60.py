from lib.prime import sieve
import networkx as nx
from itertools import combinations, product
from sympy.ntheory.primetest import isprime

max_prime = 10**5
target_n = 5

primes = sieve(max_prime)
prime_set = set(primes)

def is_concat_prime(n1, n2):
  return isprime(int(str(n1) + str(n2))) and isprime(int(str(n2) + str(n1)))

G = nx.Graph()

def calculate():
  for i, p1 in enumerate(primes[1:], 1):
    edges_added = 0
    for p2 in primes[:i]:
      if is_concat_prime(p1, p2):
        G.add_edge(p1, p2)
        edges_added += 1
    if edges_added >= target_n - 1:
      # Hunt for a clique of size target_n by brute force
      neighbors = nx.neighbors(G, p1)
      for candidates in combinations(neighbors, target_n - 1):
        edges = [G.has_edge(*e) for e in combinations(candidates, 2)]
        if all(edges):
          solution = list(candidates) + [p1]
          print("Found solution: {} sum={}".format(solution, sum(solution)))
          return

calculate()