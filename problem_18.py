input_text = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

lines = input_text.strip().splitlines()

lattice = [[int(x) for x in line.split()] for line in lines]

def left_parent(lattice, row_i, col_j):
  if col_j == 0:
    return 0 # won't affect sum later
  else:
    return lattice[row_i - 1][col_j - 1]

def right_parent(lattice, row_i, col_j):
  try:
    return lattice[row_i - 1][col_j]
  except IndexError:
    return 0 # won't affect sum later

# Make a new lattice of the same shape to hold the maximum-sum path to each vertex
best_path_lattice = [[0 for _ in row] for row in lattice]

for row_i, line in enumerate(lattice):
  for col_j, value in enumerate(line):
    left_incoming = left_parent(best_path_lattice, row_i, col_j)
    right_incoming = right_parent(best_path_lattice, row_i, col_j)
    best_incoming = max(left_incoming, right_incoming)
    best_path_lattice[row_i][col_j] = best_incoming + value

print(best_path_lattice)
print(max(best_path_lattice[-1]))
