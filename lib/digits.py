def digits_to_num(digits):
  '''Accepts digits as either numbers or strings'''
  return sum([int(d)*10**i for i, d in enumerate(reversed(digits))])