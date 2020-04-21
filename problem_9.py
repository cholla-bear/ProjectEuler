from math import ceil

def pythagorean_triple_sum_1000():
  for a in range(1, 333):
    for b in range(a, ceil((1000+a)/2)):
      c = 1000 - a - b
      if a**2 + b**2 == c**2:
        print("a={} b={} c={}".format(a,b,c))
        print(a*b*c)
        return

pythagorean_triple_sum_1000()