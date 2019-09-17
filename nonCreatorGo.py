import Input
import time
import random
import RandomV

# 0xC8 up
# 0xCB left
# 0xD0 down
# 0xCD right


def goUp():
    Input.PressKey(0xC8)
    Input.PressKey(0xCB)
    time.sleep(max(0.1,random.gauss(0.8,0.1)))
    Input.ReleaseKey(0xCB)
    Input.PressKey(0xCD)
    time.sleep(max(0.1,random.gauss(0.8,0.1)))
    Input.ReleaseKey(0xCD)
    Input.ReleaseKey(0xC8)


def goDown():
    Input.PressKey(0xD0)
    Input.PressKey(0xCB)
    time.sleep(max(0.1,random.gauss(0.8,0.1)))
    Input.ReleaseKey(0xCB)
    Input.PressKey(0xCD)
    time.sleep(max(0.1,random.gauss(0.8,0.1)))
    Input.ReleaseKey(0xCD)
    Input.ReleaseKey(0xD0)


def goLeft():
    Input.PressKey(0xCB)
    Input.PressKey(0xC8)
    time.sleep(max(0.1,random.gauss(0.8,0.1)))
    Input.ReleaseKey(0xC8)
    Input.PressKey(0xD0)
    time.sleep(max(0.1,random.gauss(0.8,0.1)))
    Input.ReleaseKey(0xD0)
    Input.ReleaseKey(0xCB)


def goRight():
    Input.PressKey(0xCD)
    Input.PressKey(0xC8)
    time.sleep(max(0.1,random.gauss(0.8,0.1)))
    Input.ReleaseKey(0xC8)
    Input.PressKey(0xD0)
    time.sleep(max(0.1,random.gauss(0.8,0.1)))
    Input.ReleaseKey(0xD0)
    Input.ReleaseKey(0xCD)

