import time
import pyautogui


while True:
    x,y = pyautogui.position()
    print('%d'%(x) + ',' + '%d'%(y))
    time.sleep(1)