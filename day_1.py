from aocd import data
from itertools import count
dl = [int(n) for n in data.split()]
a = sum(dl)

def freq_collision(dl_c):
    dl_c_len = len(dl_c)
    freq = 0
    seen_freq = [freq]

    for i in count(0):
        freq += dl_c[i % dl_c_len]
        if freq in seen_freq:
            break
        seen_freq.append(freq)
    return freq

ex1 = [1, -1]
ex2 = [3, 3, 4, -2, -4]

assert 0 == freq_collision(ex1)
assert 10 == freq_collision(ex2)

b = freq_collision(dl)

print("A: {}".format(a))
print("B: {}".format(b))
