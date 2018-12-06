from aocd import data
from itertools import repeat, starmap

def remove_matchy_matchy(d):
    for i in range(len(d) - 1):
        if d[i].lower() == d[i+1].lower() and d[i].islower() != d[i+1].islower():
            return d[:i] + d[i+2:]
    return d

def stripped(d, l):
    n = d.replace(l, '').replace(l.upper(), '')
    return part_a(n)

def part_a(d):
    while True:
      new = remove_matchy_matchy(d)
      if new == d:
        return len(new)
      d = new

def part_b(d):
    scores = starmap(stripped, zip(repeat(d), set(d.lower())))
    return min(scores)

def part_a_faster(units):
  # Someone else's version from reddit that is way more efficient. Storing here for posterity
  # https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4iuqo 
  new_units = []
  for i in range(len(units)):
    if len(new_units) > 0 and abs(ord(units[i])-ord(new_units[-1])) == 32:
      new_units.pop()
    else:
      new_units.append(units[i])
  return len(new_units)


ex1 = 'dabAcCaCBAcCcaDA'

assert part_a(ex1) == 10
print("A: {}".format(part_a(data)))

assert part_b(ex1) == 4
print("B: {}".format(part_b(data)))