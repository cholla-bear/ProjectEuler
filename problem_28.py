from itertools import islice

def number_spiral_corners():
  n = 1
  yield n

  ring = 1
  corner = 0 # Bottom right

  while True:
    if corner > 3: # Top right
      ring += 1
      corner = 0
    skip_amount = 2*ring
    n += skip_amount
    corner += 1
    # print("n={} ring={} corner={}".format(n, ring, corner))
    yield n

board_size = 1001
number_of_items = 1 + 2*(board_size - 1)
corner_gen = number_spiral_corners()
sum_of_diagonals = sum(islice(corner_gen, number_of_items))

print(sum_of_diagonals)