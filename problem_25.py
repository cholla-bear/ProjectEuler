def fib():
  (a, b) = (1, 1)
  while True:
    yield a
    (a, b) = (b, a + b)

def num_digits(n):
  return len(str(n))

def first_with_n_digits(n, seq):
  index, val = next(filter(lambda x: num_digits(x[1]) >= n, enumerate(seq)))
  return index, val

index, _ = first_with_n_digits(1000, fib())
print(index + 1)