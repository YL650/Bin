import random
import math
import CreatorGo


def rdp3():  # random .3
    x = max(0.1, random.gauss(0.3, 0.05))
    return x


def rd1():  # random 1
    x = max(0.1, random.gauss(1, 0.1))
    return x

def rd2():  # random 2
    x = max(1.7, random.gauss(2,0.1))
    return x

def randomWalk(t):  # random Walk
    for i in range(1,t+1):
        a = random.uniform(1,5)
        a = min(4,math.floor(a))
        if a == 1:
            CreatorGo.goUp(1,400,300)
        if a == 2:
            CreatorGo.goDown(1,400,300)
        if a == 3:
            CreatorGo.goRight(1,400,300)
        if a == 4:
            CreatorGo.goLeft(1,400,300)

def oneDirectionRandomWalk(t):  # random Walk
    a = random.uniform(1,5)
    a = min(4,math.floor(a))
    if a == 1:
        CreatorGo.goUp(t,400,300)
    if a == 2:
        CreatorGo.goDown(t,400,300)
    if a == 3:
        CreatorGo.goRight(t,400,300)
    if a == 4:
        CreatorGo.goLeft(t,400,300)
    return a
