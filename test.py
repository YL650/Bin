import random
import time
import CreatorDowntownNavigation
import pyautogui
import cv2
import numpy as np
from PIL import Image
from PIL import ImageOps
import CreatorDungeon
import CreatorGo
import Input

# pil_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
# pil_image = Image.fromarray(pil_image)

time.sleep(2)
p = time.time()

# im = pyautogui.screenshot()
# im = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
# cv2.imshow('x',im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# screenshot = pyautogui.screenshot(r'C:\Users\Administrator\Desktop\scr.png', region=(0, 0, 800, 600))
# opencv_screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
# pil_array = cv2.cvtColor(opencv_screenshot,cv2.COLOR_BGR2RGB)
# pil_image = Image.fromarray(pil_array)
# print(pil_image == r'C:\Users\Administrator\Desktop\scr.png')
#
# default_monster = cv2.imread(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Monster.png')
# PIL_default_monster = cv2.cvtColor(default_monster, cv2.COLOR_BGR2RGB)
# PIL_default_monster = Image.fromarray(PIL_default_monster)



# all_rgb_codes = opencv_screenshot.reshape(-1, opencv_screenshot.shape[-1])
# unique_rgbs = np.unique(all_rgb_codes, axis=0, return_counts=True)
# colors = unique_rgbs[0]
# counts = unique_rgbs[1]
# for i in range(0,len(colors)):
#     if counts[i]>1000:
#         print(colors[i] == [0,0,0])
# print(counts)



# opencv_image = np.zeros((50,20,3), np.uint8)
# opencv_image[:,:] = [24, 231, 123]
# cv2.imshow('im', opencv_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# pil_image=cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
# pil_image = Image.fromarray(pil_image)




# T = list(pyautogui.pLocate(pil_image,r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Monster.png'))
# print(T)

CreatorDungeon.ClearRoom()









q = time.time()
print(q-p)
