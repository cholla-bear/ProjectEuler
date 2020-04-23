def sum_digits(n):
  return sum((int(x) for x in str(n)))

print(sum_digits(2**1000))