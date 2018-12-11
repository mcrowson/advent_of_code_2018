from collections import deque

def partsab(players, last):
    scores = [0 for _ in range(players)]
    q = deque([0])

    for marble in range(1, last + 1):
        if marble % 23 == 0:
            q.rotate(7)
            scores[marble % players] += marble + q.pop()
            q.rotate(-1)
        else:
            q.rotate(-1)
            q.append(marble)

    return max(scores)


assert partsab(players=9, last=25) == 32
assert partsab(players=10, last=1618) == 8317
assert partsab(players=13, last=7999) == 146373
assert partsab(players=17, last=1104) == 2764
assert partsab(players=21, last=6111) == 54718
assert partsab(players=30, last=5807) == 37305
print("A: {}".format(play_game(players=441, last=71032)))
print("B: {}".format(play_game(players=441, last=71032 * 100)))
