input_text = ""

with open('p067_triangle.txt') as fh:
  input_text = fh.read()

# Copy-paste from problem 18

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