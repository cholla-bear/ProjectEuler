from functools import lru_cache

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

@lru_cache(maxsize=None)
def fill(value, available_coins):
  coin_value = available_coins[0]
  if coin_value == 1:
    return 1 # only one way to finish
  max_count = int(value/coin_value)
  found_ways = 0
  for n in range(max_count + 1):
    remaining_value = value - n*coin_value
    if remaining_value == 0:
      found_ways += 1
    else:
      found_ways += fill(remaining_value, available_coins[1:])
  return found_ways

print(fill(200, tuple(reversed(coin_values))))
