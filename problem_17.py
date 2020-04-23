import re

digits = {
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
}

teens = {
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
}

tens = {
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
}

powers = {
  100: 'hundred',
  1000: 'thousand',
}

def num_to_words(n):
  if n == 0:
    return 'zero'
  elif n < 10:
    return digits[n]
  elif n < 20:
    return teens[n]
  elif n < 100:
    tens_place, ones_place = divmod(n, 10)
    if ones_place:
      return tens[tens_place*10] + '-' + digits[ones_place]
    else:
      return tens[tens_place*10]
  elif n < 1000:
    hundreds_place, remainder = divmod(n, 100)
    if remainder:
      return digits[hundreds_place] + " hundred and " + num_to_words(remainder)
    else:
      return digits[hundreds_place] + " hundred"
  elif n == 1000:
    return "one thousand"

concatenated = "".join((num_to_words(n) for n in range(1,1001)))
print(len(re.sub(r'\W+', '', concatenated)))