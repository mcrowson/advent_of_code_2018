from aocd import data
from collections import defaultdict
import re
import numpy as np

dl = data.split('\n')


def part_a(data):
    p = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    fabric_map = np.matrix(np.zeros((2000, 2000)))
    for row in data:
        idn, l, t, w, h = p.match(row).groups()
        idn, l, t, w, h = map(int, [idn, l, t, w, h])
        fabric_map[t:t+h, l:l+w] += 1

    return (fabric_map > 1).sum()


def part_b(data):
    p = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    fabric_map = np.array(np.zeros((2000, 2000)))
    no_conflict = set()
    for row in data:
        idn, l, t, w, h = p.match(row).groups()
        idn, l, t, w, h = map(int, [idn, l, t, w, h])
        if np.all(fabric_map[t:t+h, l:l+w] == 0):
            no_conflict.add(idn)
        else:
            conflicts = np.unique(fabric_map[t:t+h, l:l+w])
            [no_conflict.remove(c) for c in conflicts if c in no_conflict]
        fabric_map[t:t+h, l:l+w] = idn 

    return next(iter(no_conflict))


ex1 = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2']

assert part_a(ex1) == 4
print("A: {}".format(part_a(dl)))

assert part_b(ex1) == 3
print("B: {}".format(part_b(dl)))