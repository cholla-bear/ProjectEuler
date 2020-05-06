import numpy as np

grid_size = 21

# Grid will represent number of ways to get to each vertex
grid = np.zeros((grid_size, grid_size), dtype=int)

# Only one way to get to the top row or left column
grid[0, :] = 1
grid[:, 0] = 1

# The number of ways to reach each vertex is the sum of the
# ways to reach the vertices to the left of and above it
for i in range(1, grid_size):
  for j in range(1, grid_size):
    grid[i,j] = grid[i-1, j] + grid[i, j-1]

print(grid[-1, -1])