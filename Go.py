import Input
import time
import random

# 0xC8 up
# 0xCB left
# 0xD0 down
# 0xCD right


def goUp(t):
    Input.PressKey(0xC8)
    Input.PressKey(0xCD)
    time.sleep(max(0.05,random.gauss(t/2,0.05)))
    Input.ReleaseKey(0xCD)
    Input.PressKey(0xCB)
    time.sleep(max(0.05,random.gauss(t/2,0.05)))
    Input.ReleaseKey(0xCB)
    Input.ReleaseKey(0xC8)


def goDown(t):
    Input.PressKey(0xD0)
    Input.PressKey(0xCD)
    time.sleep(max(0.05,random.gauss(t/2,0.05)))
    Input.ReleaseKey(0xCD)
    Input.PressKey(0xCB)
    time.sleep(max(0.05,random.gauss(t/2,0.05)))
    Input.ReleaseKey(0xCB)
    Input.ReleaseKey(0xD0)


def goLeft(t):
    Input.PressKey(0xCB)
    Input.PressKey(0xD0)
    time.sleep(max(0.05,random.gauss(t/2,0.05)))
    Input.ReleaseKey(0xD0)
    Input.PressKey(0xC8)
    time.sleep(max(0.05,random.gauss(t/2,0.05)))
    Input.ReleaseKey(0xC8)
    Input.ReleaseKey(0xCB)


def goRight(t):
    Input.PressKey(0xCD)
    Input.PressKey(0xD0)
    time.sleep(max(0.05,random.gauss(t/2,0.05)))
    Input.ReleaseKey(0xD0)
    Input.PressKey(0xC8)
    time.sleep(max(0.05,random.gauss(t/2,0.05)))
    Input.ReleaseKey(0xC8)
    Input.ReleaseKey(0xCD)

