from itertools import count

def num_digits(n):
  return len(str(n))

solution_count = 0

for n in count(1):
  if num_digits(9**n) < n:
    # No further powers of 9 will have enough digits
    break
  for i in range(1, 10):
    # Only bases in range(1, 10) can work, since
    # bases >= 10 will yield too many digits
    if num_digits(i**n) == n:
      solution_count += 1
      print("{} = {}**{}".format(i**n, i, n))

print("count={}".format(solution_count))