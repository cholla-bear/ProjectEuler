n_max = 100
limit = 10**6
count = 0
max_value = 0

prev_row = [0] * (n_max + 1)
next_row = [0] * (n_max + 1)
prev_row[0] = 1

# Binomial coefficients by Pascal's Triangle
for n in range(1, n_max + 1):
  next_row[0] = 1
  for k in range(1, n + 1):
    next_row[k] = prev_row[k] + prev_row[k-1]
    if next_row[k] > limit:
      count += 1
  prev_row = next_row
  next_row = [0] * (n_max + 1)

print(count)