from math import ceil, log10

numerals = set([str(i) for i in range(1,10)])

pandigital_products = set()

# The bounds of iteration are tricky
# We see that if i*j == k then:
# digits(k) >= digits(i) + digits(j) - 1
# Since i >= 10^(digits(i) - 1)
# So making a table:
# digits(i) + digits(j) + digits(k) >= 9:
#        1           4           4
#        2           3           4
#        3           2           4
# We'll catch all the valid combinations with
# 2-digit i and 4-digit k

for i in range(1, 100):

  # Compute an upper bound for j based on the fact that k
  # is always 4 digits, and constructing the biggest possible
  # k given the digits not included in i
  remaining_digits = numerals - set(str(i))

  biggest_4 = sorted(list(remaining_digits), reverse=True)[:4]
  biggest_k = sum([int(d)*10**i for i, d in enumerate(reversed(biggest_4))])
  upper_bound = ceil(biggest_k / i)

  lowest_4 = sorted(list(remaining_digits))[:4]
  lowest_k = sum([int(d)*10**i for i, d in enumerate(reversed(lowest_4))])
  lower_bound = int(lowest_k / i)

  for j in range(lower_bound, upper_bound):
    k = i*j
    digits = str(i) + str(j) + str(k)
    if len(digits) == 9 and set(digits) == numerals:
      print("{} * {} = {}".format(i, j, k))
      pandigital_products.add(k)

print(pandigital_products)
print("sum = {}".format(sum(pandigital_products)))