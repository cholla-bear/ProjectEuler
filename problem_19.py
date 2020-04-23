
def calendar():
  date = {'year': 1900, 'month': 1, 'day': 1, 'day_of_week': 1}
  while True:
    yield date
    date = next_date(date)

def next_date(date):
  months_30d = [4, 6, 9, 11]
  pass