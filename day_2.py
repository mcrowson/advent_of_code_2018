from aocd import data

dl = data.split()


def part_a(data):
    exactly_two = sum([1 for row in data if any([row.count(u) == 2 for u in set(row)])])
    exactly_three = sum([1 for row in data if any([row.count(u) == 3 for u in set(row)])])
    return exactly_two * exactly_three

def part_b(data):
    matches = []

    for da in data:
        d_pos = data.index(da)
        for other in data[d_pos+1:]:
            match = [d for d, o in zip(da, other) if d == o]
            matches.append(match)

    return ''.join(max(matches, key=len))

ex1 = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab']

assert part_a(ex1) == 12
print("A: {}".format(part_a(dl)))

ex2 = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz',
]

assert part_b(ex2) == 'fgij'
print("B: {}".format(part_b(dl)))