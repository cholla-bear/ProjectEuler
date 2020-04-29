coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

found_ways = 0

def fill(value, available_coins, coins_so_far):
  if len(available_coins) == 0:
    return
  coin_value = available_coins[0]
  max_count = int(value/coin_value)
  for n in range(max_count + 1):
    new_coins = coins_so_far.copy()
    new_coins[coin_value] = n
    remaining_value = value - n * coin_value
    if remaining_value == 0:
      global found_ways
      found_ways += 1
    else:
      fill(remaining_value, available_coins[1:], new_coins)

fill(200, list(reversed(coin_values)), {})

print(found_ways)