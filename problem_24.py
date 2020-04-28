from math import factorial

def nth_permutation_iter(n):
  available_digits = list(range(0,10))

  digits = []
  remainder = n

  for i in range(10,0,-1):
    # there are factorial(i-1) permutations keeping this digit
    # constant, so we can use this to work out the value of
    # the current digit
    digit_index, remainder = divmod(remainder, factorial(i-1))
    digit = available_digits[digit_index]
    digits.append(digit)
    available_digits.remove(digit)

  return digits

def nth_permutation(n):
  available_digits = list(range(0,10))
  return nth_permutation_recursive(n, available_digits)

def nth_permutation_recursive(n, available_digits):
  if len(available_digits) == 1:
    return available_digits
  # Number of permutations with the top digit fixed
  p = factorial(len(available_digits) - 1)
  digit_index, remainder = divmod(n, p)
  digit = available_digits[digit_index]
  available_digits.remove(digit)
  return [digit] + nth_permutation_recursive(remainder, available_digits)

print(nth_permutation(1))