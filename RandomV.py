import random
import math
import Go

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
            Go.goUp(1)
        if a == 2:
            Go.goDown(1)
        if a == 3:
            Go.goRight(1)
        if a == 4:
            Go.goLeft(1)