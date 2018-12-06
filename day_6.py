from aocd import data
import numpy as np

def manhattan(pairs, grid):
    res = []
    
    return res

def part_a(d):
    pairs = [l.split(', ') for l in d]
    p_ar = np.array(pairs).astype(np.integer)  # 2D array of points
    li_x, li_y = p_ar[:,0].min()-1, p_ar[:,1].min()-1 # Low Infinity X/Y
    hi_x, hi_y = p_ar[:,0].max()+1, p_ar[:,1].max()+1  # High Infinity X/Y
    grid = np.mgrid[li_x:hi_x + 1, li_y:hi_y + 1].reshape(2, -1).T  # Grid with 1 beyond min/max for infinity
    i = [] 
    # Identify the closest point for each space on the grid
    for cell in grid:
      closest = None
      distance = 9999999
      for p in pairs:
        d = sum(abs(int(a)-int(b)) for a,b in zip(cell, p))
        if d < distance:
          distance = d
          closest = p
        elif d == distance:
          closest = ['0', '0'] # Duplicate match 
      i.append(tuple(closest))
    
    # Find the pairs that go to infinity so we can discount them
    touches_infinity = set()
    for n, p in enumerate(grid):
      if np.any([p[0] == li_x, p[0] == hi_x, p[1] == li_y, p[1] == hi_y]):
        touches_infinity.add(i[n])

    # Subset of grid that does not touch pairs that go to infinity
    closeness = [n for n in i if n not in touches_infinity]
    return max([closeness.count(n) for n in set(closeness)])

def part_b(d, thresh):
    pairs = [l.split(', ') for l in d]
    p_ar = np.array(pairs).astype(np.integer)  # 2D array of points
    li_x, li_y = p_ar[:,0].min()-1, p_ar[:,1].min()-1 # Low Infinity X/Y
    hi_x, hi_y = p_ar[:,0].max()+1, p_ar[:,1].max()+1  # High Infinity X/Y
    grid = np.mgrid[li_x:hi_x + 1, li_y:hi_y + 1].reshape(2, -1).T  # Grid with 1 beyond min/max for infinity
    distances = [sum([sum(abs(int(a)-int(b)) for a,b in zip(cell, p)) for p in pairs]) for cell in grid]
    return sum([1 for d in distances if d < thresh ])

    
ex1 = ['1, 1',
       '1, 6',
       '8, 3',
       '3, 4',
       '5, 5',
       '8, 9']

assert part_a(ex1) == 17
print("A: {}".format(part_a(data.split('\n'))))

assert part_b(ex1, 32) == 16
print("B: {}".format(part_b(data.split('\n'), 10000)))