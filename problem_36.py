from itertools import count, takewhile

def even_length_palindromes():
  for i in count(1):
    yield int(str(i) + str(i)[::-1])

def odd_length_palindromes():
  for i in range(10):
    yield i
  for i in count(1):
    for j in range(10):
      yield int(str(i) + str(j) + str(i)[::-1])

def is_binary_palindrome(n):
  n_str = bin(n)[2:] # strip off "0b" prefix
  return n_str == n_str[::-1]

def sum_palindromes(limit, iterable):
  return sum(
    filter(
      is_binary_palindrome,
      takewhile(
        lambda x: x < limit,
        iterable
      )
    )
  )

limit = 1000000
sum_even = sum_palindromes(limit, even_length_palindromes())
sum_odd = sum_palindromes(limit, odd_length_palindromes())

print(sum_even + sum_odd)