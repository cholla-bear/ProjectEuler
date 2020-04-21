from functools import reduce
from operator import add

def sum_squares(n):
  return reduce(add, (x**2 for x in range(1, n+1)))

def square_sum(n):
  return (sum(range(1, n+1)))**2

print(square_sum(100) - sum_squares(100))