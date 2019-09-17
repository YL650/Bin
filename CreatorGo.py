import Input
import time
import random
import RandomV

# 0x11 up
# 0x1E left
# 0x1F down
# 0x20 right


def goUp(t,x,y):
    # if forward is on the left we go right first
    if x<400:
        Input.PressKey(0x11)
        Input.PressKey(0x20)
        time.sleep(max(0.05, random.gauss(t / 2, t/20)))
        Input.ReleaseKey(0x20)
        Input.PressKey(0x1E)
        time.sleep(max(0.05, random.gauss(t / 2, t/20)))
        Input.ReleaseKey(0x1E)
        Input.ReleaseKey(0x11)
    else: # vice-versa
        Input.PressKey(0x11)
        Input.PressKey(0x1E)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x1E)
        Input.PressKey(0x20)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x20)
        Input.ReleaseKey(0x11)


def goDown(t,x,y):
    # if forward is on the left we go right first
    if x<400:
        Input.PressKey(0x1F)
        Input.PressKey(0x20)
        time.sleep(max(0.05, random.gauss(t / 2, t/20)))
        Input.ReleaseKey(0x20)
        Input.PressKey(0x1E)
        time.sleep(max(0.05, random.gauss(t / 2, t/20)))
        Input.ReleaseKey(0x1E)
        Input.ReleaseKey(0x1F)
    else: # vice-versa
        Input.PressKey(0x1F)
        Input.PressKey(0x1E)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x1E)
        Input.PressKey(0x20)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x20)
        Input.ReleaseKey(0x1F)


def goLeft(t,x,y):
    if y<380: # if forward is above go down first
        Input.PressKey(0x1E)
        Input.PressKey(0x1F)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x1F)
        Input.PressKey(0x11)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x11)
        Input.ReleaseKey(0x1E)
    else: # vice-versa
        Input.PressKey(0x1E)
        Input.PressKey(0x11)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x11)
        Input.PressKey(0x1F)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x1F)
        Input.ReleaseKey(0x1E)


def goRight(t,x,y):
    if y<380:
        Input.PressKey(0x20)
        Input.PressKey(0x1F)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x1F)
        Input.PressKey(0x11)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x11)
        Input.ReleaseKey(0x20)
    else:
        Input.PressKey(0x20)
        Input.PressKey(0x11)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x11)
        Input.PressKey(0x1F)
        time.sleep(max(0.05,random.gauss(t/2,t/20)))
        Input.ReleaseKey(0x1F)
        Input.ReleaseKey(0x20)
