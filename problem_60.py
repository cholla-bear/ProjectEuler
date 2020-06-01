from lib.prime import sieve
import networkx as nx

max_prime = 10**8
target_n = 5

primes = sieve(max_prime)
prime_set = set(primes)

print("done computing primes")

def is_prime(n):
  return n in prime_set

def is_concat_prime(n1, n2):
  return is_prime(int(str(n1) + str(n2))) and is_prime(int(str(n2) + str(n1)))

G = nx.Graph()

def calculate():
  for i, p1 in enumerate(primes[1:], 1):
    for p2 in primes[:i]:
      if is_concat_prime(p1, p2):
        G.add_edge(p1, p2)
    cliques = nx.cliques_containing_node(G, p2)
    for clique in cliques:
      if len(clique) == target_n:
        print("Found solution {} sum={}".format(clique, sum(clique)))
        return

calculate()