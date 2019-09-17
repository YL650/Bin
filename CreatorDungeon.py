import cv2
from PIL import Image

import CreatorGo
import pyautogui
import Input
import time
import numpy as np
import threading
import CreatorRandomV
import queue
import random

def getSelfPos():
    x, y = pyautogui.monochromeLocateCenterOnScreen(
        r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\SelfPos2.png',
        region=(0, 0, 800, 600))
    return x-22, y+90


def whetherDetect(path, fourtuple):
    try:
        x, y = pyautogui.pLocateCenterOnScreen(path, region=fourtuple)
        T = 1
    except:
        T = 0
    return T


def monochromeWhetherDetect(path, fourtuple):
    try:
        x, y = pyautogui.monochromeLocateCenterOnScreen(path, region=fourtuple)
        T = 1
    except:
        T = 0
    return T


def whetherLocate(needle, haystack):
    L = list(pyautogui.locateAll(needle, haystack))
    if len(L) > 0:
        return True
    else:
        return False


def whetherPLocate(needle, haystack):
    L = list(pyautogui.pLocateAll(needle, haystack))
    if len(L) > 0:
        return True
    else:
        return False


def buff():
    Input.KeyPress(0x2C)


def TestZeroMat(A):  # we use it to test whether any monster is left not slayed
    if len(A) == 10 and len(A[0]) == 16:
        zeros = np.zeros((10, 16), dtype='i')
        C = (A == zeros)
        for i in range(1, 10):
            for j in range(1, 16):
                if not C[i][j]:
                    return False
    else:
        print('the matrix has wrong dimension')
    return True


def Stay():  # set-off side effects of PesudoRandomWalk
    Input.ReleaseKey(0x11)
    Input.ReleaseKey(0x1F)
    Input.ReleaseKey(0x20)
    Input.ReleaseKey(0x1E)


def Initialization():
    if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\QuestDungeon.png',
                     (0, 0, 800, 600)) == 1:  # choose quest dungeon
        x, y = pyautogui.locateCenterOnScreen(
            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\QuestDungeon.png', region=(0, 0, 800, 600))
        pyautogui.moveTo(x, y)
        Input.click()
    elif whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Loading.png',
                       (0, 450, 800, 150)) == 1:
        time.sleep(5)
    elif whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\CreatorBuff.png',
                       (91, 509, 200, 60)) == 0:
        buff()
    elif whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\NPKDialogue.png',
                       (0, 0, 800, 600)) == 1:
        Input.KeyPress(0x01)
        time.sleep(0.2)
        Input.KeyPress(0x39)
        time.sleep(0.3)
    elif whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\QuestDungeon2.png',
                       (0, 0, 800, 600)) == 1:
        x, y = pyautogui.locateCenterOnScreen(
            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\QuestDungeon2.png', region=(0, 0, 800, 600))
        pyautogui.moveTo(x, y)
        time.sleep(0.3)
        Input.click()


def GridCoordinate(x, y):  # we partition the interface into 50x60 boxes, the output is in matrix representation
    if x < 800:
        v1 = x // 50
    else:
        v1 = 15
    if y < 600:
        v2 = y // 60
    else:
        v2 = 9
    return v2, v1


def DMGDetect():
    L = list(
        pyautogui.pLocateAllOnScreen(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\DamageFont.png',
                                     region=(0, 0, 800, 600)))
    DMGPos = np.zeros((10, 16), dtype='i')
    for i in range(0, len(L)):  # decide the location of DMGFonts in a screen
        temp_x, temp_y = pyautogui.center(L[i])
        y, x = GridCoordinate(temp_x, temp_y)
        DMGPos[y][x] = 1
    return DMGPos


def SelfGridPos():
    try:
        temp_x, temp_y = pyautogui.monochromeLocateCenterOnScreen2(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\SelfPos2.png',
                                         region=(0, 0, 800, 600))
        temp_x = temp_x - 22
        temp_y = temp_y + 90
        avatar_y, avatar_x = GridCoordinate(temp_x, temp_y)
        return avatar_y, avatar_x
    except:
        CreatorRandomV.randomWalk(2)
        return SelfGridPos()


def CollectItem():
    try:
        while True:
            if monochromeWhetherDetect(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Gold.png',
                    (0, 0, 600, 530)) == 1:
                x, y = pyautogui.monochromeLocateCenterOnScreen(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Gold.png',
                    region=(0, 0, 600, 530))
                pyautogui.moveTo(x - 6, y)
                Input.click()

            elif monochromeWhetherDetect(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item1.png',
                    (0, 0, 600, 530)) == 1:
                x, y = pyautogui.monochromeLocateCenterOnScreen(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item1.png',
                    region=(0, 0, 600, 530))
                pyautogui.moveTo(x, y)
                Input.click()

            elif monochromeWhetherDetect(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item2.png',
                    (0, 0, 600, 530)) == 1:
                x, y = pyautogui.monochromeLocateCenterOnScreen(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item2.png',
                    region=(0, 0, 600, 530))
                pyautogui.moveTo(x + 40, y)
                Input.click()

            elif monochromeWhetherDetect(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item3.png',
                    (0, 0, 600, 530)) == 1:
                x, y = pyautogui.monochromeLocateCenterOnScreen(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item3.png',
                    region=(0, 0, 600, 530))
                pyautogui.moveTo(x, y)
                Input.click()

            elif monochromeWhetherDetect(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item4.png',
                    (0, 0, 600, 530)) == 1:
                x, y = pyautogui.monochromeLocateCenterOnScreen(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item4.png',
                    region=(0, 0, 600, 530))
                pyautogui.moveTo(x - 20, y)
                Input.click()

            elif monochromeWhetherDetect(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item5.png',
                    (0, 0, 600, 530)) == 1:
                x, y = pyautogui.monochromeLocateCenterOnScreen(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item5.png',
                    region=(0, 0, 600, 530))
                pyautogui.moveTo(x, y)
                Input.click()

            elif monochromeWhetherDetect(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item6.png',
                    (0, 0, 600, 530)) == 1:
                x, y = pyautogui.monochromeLocateCenterOnScreen(
                    r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Item\Item6.png',
                    region=(0, 0, 600, 530))
                pyautogui.moveTo(x, y)
                Input.click()

            else:
                return
    except:
        return


def ClearScreenDodging(color):

    def AttackGrid(Gridy, Gridx):
        if not (0 < 25 + 50 * Gridx < 100 and 95 < 30 + 60 * Gridy < 131) and not (
                580 < 25 + 50 * Gridx < 800 and 150 < 30 + 60 * Gridy < 420):
            pyautogui.moveTo(25 + 50 * Gridx, 30 + 60 * Gridy)
            for i in range(0, 10):
                Input.click()
                Input.rclick()
        else:
            return

    # Pos = [first row, second row], gives the position of a spell in spell chart
    def spellPos(needle):
        def center(T):
            x = int(T[0] + T[2] / 2)
            y = int(T[1] + T[3] / 2)
            return x, y

        Pos = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        im = pyautogui.screenshot(region=(530, 530, 200, 30))
        L = list(pyautogui.pLocateAll(needle, im))
        if len(L) > 0:
            x, y = center(L[0])
            x = x + 530
            y = y + 530
            if y < 545:  # row 1
                if 530 < x <= 564:
                    Pos[0][0] = 1
                elif 564 < x <= 600:
                    Pos[0][1] = 1
                elif 600 < x <= 637:
                    Pos[0][2] = 1
                elif 637 < x <= 672:
                    Pos[0][3] = 1
                elif 672 < x <= 719:
                    Pos[0][4] = 1
            else:
                if 530 < x <= 564:
                    Pos[1][0] = 1
                elif 564 < x <= 600:
                    Pos[1][1] = 1
                elif 600 < x <= 637:
                    Pos[1][2] = 1
                elif 637 < x <= 672:
                    Pos[1][3] = 1
                elif 672 < x <= 719:
                    Pos[1][4] = 1
        return Pos

    # hotkeys are: QERFG, the method Hotkeys helps press C and gives the hotkey of the corresponding spell

    def hotkeys(spellpos):
        if spellpos[1] == [0, 0, 0, 0, 0]:
            if spellpos[0] != [0, 0, 0, 0, 0]:
                Input.KeyPress(0x2E)  # Press C
                time.sleep(0.4)
                L = spellpos[0]
                i = L.index(1)
                if i == 0:
                    return 0x10
                elif i == 1:
                    return 0x12
                elif i == 2:
                    return 0x13
                elif i == 3:
                    return 0x21
                elif i == 4:
                    return 0x22
            else:
                return 0
        else:
            L = spellpos[1]
            i = L.index(1)
            if i == 0:
                return 0x10
            elif i == 1:
                return 0x12
            elif i == 2:
                return 0x13
            elif i == 3:
                return 0x21
            elif i == 4:
                return 0x22

    def ice(Gridy, Gridx):
        if not (0 < 25 + 50 * Gridx < 50 and 95 < 30 + 60 * Gridy < 131) and not (
                580 < 25 + 50 * Gridx < 800 and 150 < 30 + 60 * Gridy < 420):
            flag = 0
            Pos = spellPos(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Spells\Ice.png')
            hk = hotkeys(Pos)
            if hk != 0:
                flag = 1
                Input.KeyPress(hk)
                time.sleep(0.5)
                pyautogui.moveTo(25 + 50 * Gridx, 30 + 60 * Gridy)
                for i in range(0, 10):
                    Input.click()
                    Input.rclick()
                Input.KeyPress(hk)
        else:
            flag = 1
        return flag

    def shield():
        flag = 0
        Pos = spellPos(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Spells\Shield.png')
        hk = hotkeys(Pos)
        if hk != 0:
            flag = 1
            Input.KeyPress(hk)
            time.sleep(0.5)
            Input.rclick()
            time.sleep(1)
            Input.click()
            time.sleep(4)
            Input.KeyPress(hk)
        return flag

    def wind(Gridy, Gridx):
        if not (0 < 25 + 50 * Gridx < 50 and 95 < 30 + 60 * Gridy < 131) and not (
                580 < 25 + 50 * Gridx < 800 and 150 < 30 + 60 * Gridy < 420):
            flag = 0
            Pos = spellPos(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Spells\Wind.png')
            hk = hotkeys(Pos)
            if hk != 0:
                flag = 1
                Input.KeyPress(hk)
                time.sleep(0.5)
                pyautogui.moveTo(25 + 50 * Gridx, 30 + 60 * Gridy)
                for i in range(0, 10):
                    Input.rclick()
                Input.KeyPress(hk)
        else:
            flag = 1
        return flag

    # def apocolypse(Gridy, Gridx):
    #
    # def ice_age(Gridy, Gridx):
    #
    # def void():

    def PesudoRandomWalk(stop_flag):
        i = 0
        while True:
            if stop_flag():
                break
            else:
                i = i + 1
                if i % 2 == 0:
                    CreatorGo.goUp(0.4, 400, 300)
                elif i % 2 == 1:
                    CreatorGo.goDown(0.4, 400, 300)

# color contains a list of opencv-images
    def ClearScreen(color):

        def oneRound(color):
            PossiblePos = np.zeros((10, 16), dtype='i')
            for any_color in color:
                pil_image = cv2.cvtColor(any_color, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(pil_image)
                L = list(pyautogui.pLocateAllOnScreen(pil_image, region=(0, 130, 800, 470)))
                for i in range(0, len(L)):  # decide the location of monsters in a screen
                    temp_x, temp_y = pyautogui.center(L[i])
                    y, x = GridCoordinate(temp_x, temp_y)
                    PossiblePos[y][x] = 1

            print(PossiblePos)
            while True:
                i = random.randint(0,9)
                j = random.randint(0,15)
                if PossiblePos.any() != 0:
                    if PossiblePos[i][j] == 1:
                        for k in range(i,9):
                            if PossiblePos[k+1][j] == 0:
                                i = k
                                break
                            else:
                                continue
                        break
                else:
                    return
            avatary, avatarx = SelfGridPos()
            if PossiblePos[avatary][avatarx] == 1:
                if shield() == 1:
                    print('shield')
                    return
                elif ice(avatary, avatarx) == 1:
                    print('ice')
                    return
                elif wind(avatary, avatarx) == 1:
                    print('wind')
                    return

                else:
                #places reserved for other spells
                    AttackGrid(i, j)
                    return

            else:
                # here should be a conditional clause for zero possible pos mat
                if abs(avatary - i) < 2 and abs(avatarx - j) < 2:
                    if shield() == 1:
                        print('shield')
                        return

                elif abs(avatary - i) < 3 and abs(avatarx - j) < 6:
                    if ice(i, j) == 1:
                        print('ice')
                        return

                    if wind(i, j) == 1:
                        print('wind')
                        return

                else:
                #places reserved for other spells
                    AttackGrid(i, j)
                    return

        def DMG(stopflag, ini_pos):

            ini_pos_found = False   #  this part aims to find an initial pos
            for i in range(1,10):
                a = DMGDetect()
                if a.any() != 0:
                    ini_pos.put(a)
                    ini_pos_found = True
                    break
            if not ini_pos_found:
                ini_pos.put(np.zeros((10,16), dtype='i'))

            a = DMGDetect()
            while True:
                if a.any() != 0:
                    a = DMGDetect()
                else:
                    keeplearing = False
                    for i in range(1, 8):
                        a = DMGDetect()
                        if a.any() != 0:
                            keeplearing = True
                            break
                    if not keeplearing:
                        stopflag.put(True)
                        break


        def attack(stopflag,color):
            oneRound(color)
            while True:
                if not stopflag.empty():
                    flag = stopflag.get()
                    if flag != True:
                        stopflag.put(flag)
                        oneRound(color)
                    else:
                        break
                else:
                    oneRound(color)
        ini_pos = queue.LifoQueue()
        stopflag = queue.LifoQueue()
        stopflag.put(False)
        t1 = threading.Thread(target=attack, args=(stopflag,color,))
        t2 = threading.Thread(target=DMG, args=(stopflag, ini_pos,))
        t1.start()
        time.sleep(0.5)
        t2.start()
        t1.join()
        t2.join()
        Farthest = ini_pos.get()
        return Farthest

    stop_thread = False
    t3 = threading.Thread(target=PesudoRandomWalk, args=(lambda: stop_thread,))
    t3.start()
    IniMonPos = ClearScreen(color)
    stop_thread = True
    print('we have cleared a screen while dodging')
    return IniMonPos


# note that x, y speed are 0.4s/grid, 0.3s/grid


def ClearRoom():

    def FarthestMonster(ExactMonsterPos, avatar_y, avatar_x):
        if ExactMonsterPos.any() != 0:
            FMD = 0  # FMD stands for farthest monster distance
            FarthestMonsterGrid = (8, 5)
            for j in range(0, 10):
                for k in range(0, 16):
                    if ExactMonsterPos[j][k] == 1:
                        if (j - avatar_y) * (j - avatar_y) + (k - avatar_x) * (k - avatar_x) > FMD:
                            FMD = (j - avatar_y) * (j - avatar_y) + (k - avatar_x) * (k - avatar_x)
                            FarthestMonsterGrid = (j, k)
            return FarthestMonsterGrid, (avatar_y, avatar_x)
        else:
            return (avatar_y, avatar_x),(avatar_y, avatar_x)

    def PossibleNextRoom():
        im = pyautogui.screenshot(region=(580, 0, 220, 170))
        L = list(
            pyautogui.locateAll(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\SelfPosOnMap.png', im))
        try:
            selfXonMap, selfYonMap = pyautogui.center(L[0])
            selfXonMap = selfXonMap + 580
        except:
            return [0, 0, 0, 0]
        imright = pyautogui.screenshot(region=(selfXonMap + 9, selfYonMap - 10, 16, 16))
        imleft = pyautogui.screenshot(region=(selfXonMap - 26, selfYonMap - 10, 16, 16))
        imup = pyautogui.screenshot(region=(selfXonMap - 8, selfYonMap - 27, 16, 16))
        imdown = pyautogui.screenshot(region=(selfXonMap - 8, selfYonMap + 8, 16, 16))
        start_time = time.time()
        a = [0, 0, 0, 0]  # a is priority next room index set
        while True:
            b = [0, 0, 0, 0]  # b is the index set for positions that have changed
            current_time = time.time()
            if current_time - start_time < 0.75:
                imright2 = pyautogui.screenshot(region=(selfXonMap + 9, selfYonMap - 10, 16, 16))
                imleft2 = pyautogui.screenshot(region=(selfXonMap - 26, selfYonMap - 10, 16, 16))
                imup2 = pyautogui.screenshot(region=(selfXonMap - 8, selfYonMap - 27, 16, 16))
                imdown2 = pyautogui.screenshot(region=(selfXonMap - 8, selfYonMap + 8, 16, 16))
                if not whetherPLocate(imright, imright2):  # imright has been changed
                    b[0] = 1
                    if whetherLocate(
                            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\PriorityNextRoom.png',
                            imright) or whetherLocate(
                        r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\PriorityNextRoom.png',
                        imright2):
                        a[0] = 1
                if not whetherPLocate(imleft, imleft2):  # imleft has been changed
                    b[1] = 1
                    if whetherLocate(
                            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\PriorityNextRoom.png',
                            imleft) or whetherLocate(
                        r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\PriorityNextRoom.png', imleft2):
                        a[1] = 1
                if not whetherPLocate(imup, imup2):  # imup has been changed
                    b[2] = 1
                    if whetherLocate(
                            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\PriorityNextRoom.png',
                            imup) or whetherLocate(
                        r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\PriorityNextRoom.png', imup2):
                        a[2] = 1
                if not whetherPLocate(imdown, imdown2):  # imdown has been changed
                    b[3] = 1
                    if whetherLocate(
                            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\PriorityNextRoom.png',
                            imdown) or whetherLocate(
                        r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\PriorityNextRoom.png', imdown2):
                        a[3] = 1
                if a != [0, 0, 0, 0]:
                    return a
                else:
                    if b == [0, 0, 0, 0]:
                        continue
                    else:
                        c = [0, 0, 0, 0]  # c is 'goable' index set
                        if (whetherPLocate(
                                r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\NextRoom.png',
                                imright) or whetherPLocate(
                            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\NextRoom.png',
                            imright2)) and b[0] == 1:
                            c[0] = 1
                        if (whetherPLocate(
                                r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\NextRoom.png',
                                imleft) or whetherPLocate(
                            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\NextRoom.png', imleft2)) and \
                                b[1] == 1:
                            c[1] = 1
                        if (whetherPLocate(
                                r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\NextRoom.png',
                                imup) or whetherPLocate(
                            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\NextRoom.png', imup2)) and \
                                b[2] == 1:
                            c[2] = 1
                        if (whetherPLocate(
                                r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\NextRoom.png',
                                imdown) or whetherPLocate(
                            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\NextRoom.png', imdown2)) and \
                                b[3] == 1:
                            c[3] = 1
                        return c
            else:
                return a  # 0 means we havent cleared the room

    def Go(X):
        y_distance = X[0][0] - X[1][0]
        x_distance = X[0][1] - X[1][1]
        if y_distance > 0:
            if x_distance > 0:
                CreatorGo.goRight(0.32 * x_distance, X[1][1] * 50, X[1][0] * 80)
                CreatorGo.goDown(0.45 * y_distance, X[1][1] * 50, X[1][0] * 80)
            else:
                CreatorGo.goLeft(-0.32 * x_distance, X[1][1] * 50, X[1][0] * 80)
                CreatorGo.goDown(0.45 * y_distance, X[1][1] * 50, X[1][0] * 80)
        else:
            if x_distance > 0:
                CreatorGo.goRight(0.32 * x_distance, X[1][1] * 50, X[1][0] * 80)
                CreatorGo.goUp(-0.45 * y_distance, X[1][1] * 50, X[1][0] * 80)
            else:
                CreatorGo.goLeft(-0.32 * x_distance, X[1][1] * 50, X[1][0] * 80)
                CreatorGo.goUp(-0.45 * y_distance, X[1][1] * 50, X[1][0] * 80)

    def Main(stopClearRoomFlag, colorBlocks):
        global collectFlag
        while True:
            collectFlag = False
            if not stopClearRoomFlag():  # nowait
                avatar_y, avatar_x = SelfGridPos()
                color = colorBlocks.get()
                print('length of color is %d'%len(color))
                E = ClearScreenDodging(color)  # E is initial Monster Pos
                colorBlocks.put(color)
                collectFlag = True
                if not TestZeroMat(E):
                    X = FarthestMonster(E, avatar_y, avatar_x)
                    print('furthest monster is')
                    print(X)
                    time.sleep(0.5)  # we pause the program for a bit beacuse the pesudorandamwalk thread might still be running
                    Go(X)
                else:
                    if not stopClearRoomFlag():
                        CreatorRandomV.oneDirectionRandomWalk(2)
                        'pause between two rv'
                        time.sleep(0.3)
                        CreatorRandomV.oneDirectionRandomWalk(2)
                    else:
                        break
            else:
                collectFlag = True
                break

    def collectingItems(stopClearRoomFlag):
        global collectFlag
        while True:
            if not stopClearRoomFlag():
                if collectFlag:
                    CollectItem()
            else:
                CollectItem()
                break

    def specialColorDetect(stopClearRoomFlag, colorBlocks):
        while True:
            if not stopClearRoomFlag():
                screenshot = pyautogui.screenshot(region=(0, 0, 800, 600))
                opencv_screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
                all_rgb_codes = opencv_screenshot.reshape(-1, opencv_screenshot.shape[-1])
                unique_rgbs = np.unique(all_rgb_codes, axis=0, return_counts=True)
                colors = unique_rgbs[0]
                counts = unique_rgbs[1]
                for i in range(0, len(colors)):
                    if counts[i] > 1500:
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
                                for i in range(0, len(Monster_Color)):
                                    if list(Monster_Color[i][0][0]) == list(color):
                                        Append_Flag = False
                                if Append_Flag:
                                    Monster_Color.append(opencv_image)
                                Monster_Color = np.array(Monster_Color)
                                print(len(Monster_Color))
                                colorBlocks.put(Monster_Color)
                        else:
                            continue
            else:
                break

# colorblocks contain pure color images that may be monsters
    colorBlocks = queue.LifoQueue()
    default_monster = cv2.imread(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\Monster.png')
    Monster_Color = np.array([default_monster])
    colorBlocks.put(Monster_Color)
    next_room_flag = False
    t1 = threading.Thread(target=Main, args=(lambda: next_room_flag, colorBlocks,))
    t2 = threading.Thread(target=collectingItems, args=(lambda: next_room_flag,))
    t3 = threading.Thread(target=specialColorDetect, args=(lambda: next_room_flag, colorBlocks,))
    t1.start()
    t2.start()
    t3.start()
    while True:
        a = PossibleNextRoom()
        if a == [0, 0, 0, 0]:
            time.sleep(1)
            continue
        else:
            next_room_flag = True
            break



# def dungeon():
#
#
#
#
#
#
#
#
#
