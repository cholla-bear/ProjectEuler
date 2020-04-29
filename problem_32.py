from math import ceil, log10

numerals = set([str(i) for i in range(1,10)])

pandigital_products = set()

# The bounds of iteration are tricky
# We see that if i*j == k then:
# digits(k) >= digits(i) + digits(j) - 1
# Since i >= 10^(digits(i) - 1)
# So making a table of digits(j) required to
# get digits(i) + digits(j) + digits(k) >= 9:
#        1           4           4
#        2           3           4
#        3           2           4
# We'll catch all the valid combinations with
# 2-digit i and 4-digit j

for i in range(1, 100):
  if i < 10:
    # 1-digit times 4-digit
    upper_bound = 10000
  else:
    # 2-digit times 3-digit
    upper_bound = 1000
  for j in range(i + 1, upper_bound):
    k = i*j
    digits = str(i) + str(j) + str(k)
    if len(digits) == 9 and set(digits) == numerals:
      print("{} * {} = {}".format(i, j, k))
      pandigital_products.add(k)

print(pandigital_products)
print("sum = {}".format(sum(pandigital_products)))