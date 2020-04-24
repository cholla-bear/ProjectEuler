names = []

with open('p022_names.txt') as fh:
  names = [n.strip('"') for n in fh.read().split(',')]

def char_to_num(c):
  'Return 1 for A, 2 for B, etc'
  return ord(c) - 64

def name_value(name):
  return sum([char_to_num(c) for c in name])

sum_of_scores = 0
names.sort()
for index, name in enumerate(names):
  sum_of_scores += (index + 1)*name_value(name)

print(sum_of_scores)