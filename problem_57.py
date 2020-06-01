from itertools import islice

def fraction_expansion():
  '''Continued fraction expansion for sqrt(2)'''
  n = 1
  d = 2
  while True:
    yield (n + d, d) # 1 + n/d
    (n, d) = (d, 2*d + n)

n_gt_d = filter(
  lambda x: len(str(x[0])) > len(str(x[1])),
  islice(fraction_expansion(), 1000)
)

print(len(list(n_gt_d)))