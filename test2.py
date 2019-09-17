import threading
import time
import queue
import datetime
import numpy as np
import pyautogui
import cv2
from PIL import Image

colorBlocks = queue.LifoQueue()
default_monster = cv2.imread(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Monster.png')
Monster_Color = np.array([default_monster])
colorBlocks.put(Monster_Color)

while True:
    screenshot = pyautogui.screenshot(region=(0, 0, 800, 600))
    opencv_screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    all_rgb_codes = opencv_screenshot.reshape(-1, opencv_screenshot.shape[-1])
    unique_rgbs = np.unique(all_rgb_codes, axis=0, return_counts=True)
    colors = unique_rgbs[0]
    counts = unique_rgbs[1]
    for i in range(0, len(colors)):
        if counts[i] > 1000:
            color = colors[i]
            if not (color[0] == 24 and color[1] == 231 and color[2] == 123) and not (
                    color[0] == 0 and color[1] == 0 and color[2] == 255) and not (
                    color[0] == 255 and color[1] == 0 and color[2] == 0):
                opencv_image = np.zeros((40, 60, 3), np.uint8)
                print(color)
                opencv_image[:, :] = color
                pil_image_array = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(pil_image_array)
                List = list(pyautogui.pLocateAll(pil_image, screenshot))
                if len(List) > 0:
                    Monster_Color = colorBlocks.get()
                    Monster_Color = list(Monster_Color)
                    Append_Flag = True
                    for i in range(0,len(Monster_Color)):
                        print(list(Monster_Color[i][0][0]))
                        print(list(color))
                        if list(Monster_Color[i][0][0]) == list(color):
                            Append_Flag = False
                    if Append_Flag:
                        Monster_Color.append(opencv_image)
                    Monster_Color = np.array(Monster_Color)
                    print(len(Monster_Color))
                    colorBlocks.put(Monster_Color)
            else:
                continue




