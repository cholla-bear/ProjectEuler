from functools import lru_cache

def collatz_iter(n):
  while True:
    yield n
    if n == 1:
      return
    elif n % 2 == 0:
      n = int(n/2)
    else:
      n = 3*n + 1

# Roughly 30 sec with this version on my laptop
def len_collatz_iter(n):
  return len(list(collatz_iter(n)))

# Roughly 1.6 sec
@lru_cache(maxsize=None)
def len_collatz_recur(n):
  if n == 1:
    return 1
  n_next = int(n/2) if n % 2 == 0 else 3*n + 1
  return 1 + len_collatz_recur(n_next)

def longest_collatz(n_max):
  max_len = 0
  best_n = 1

  for n in range(1, n_max):
    sequence_len = len_collatz_recur(n)
    if sequence_len > max_len:
      best_n = n
      max_len = sequence_len

  return best_n

best_n = longest_collatz(1000000) 

print("Longest sequence: n={}".format(best_n))