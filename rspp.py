from random import random

def score_rspp(p1, p2):
    """Return score for player 1 of
    Rock-Scissors-DoublePaper. Input
    is move for each player: 0 for rock,
    1 for scissors, 2 for paper.
    """
    if p1 == p2:
        return 0
    if p1 == (p2 + 1) % 3:
        if p2 == 2:
            return -2
        return -1
    else:
        if p1 == 2:
            return 2
        return 1

assert score_rspp(1, 2) == 1
assert score_rspp(0, 2) == -2
assert score_rspp(0, 1) == 1

def move(strategy):
    r = random()
    for i in range(len(strategy)):
        if r < strategy[i]:
            return i
        r -= strategy[i]
    if r < 0.01:
        return i - 1
    raise Exception("did not choose")

def sim(n, s1, s2):
    score = 0
    for _ in range(n):
        p1 = move(s1)
        p2 = move(s2)
        score += score_rspp(p1, p2)
    return score / n

s_random = [1/3, 1/3, 1/3]
s_papery = [1/4, 1/4, 1/2]
s_scissory = [1/4, 1/2, 1/4]
s_paper = [0, 0, 1]
s_scissors = [0, 1, 0]

print(sim(1000000, s_papery, s_random))
print(sim(1000000, s_paper, s_random))
print(sim(1000000, s_papery, s_scissory))
print(sim(1000000, s_random, s_scissory))
