import pyautogui
import time

import CreatorRandomV
import Input
import RandomV
import CreatorGo
import CreatorDungeon
import Login


def getForwardPos():
    x, y = pyautogui.pLocateCenterOnScreen(
        r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\Forward.png',
        region=(0, 0, 800, 600))
    return x+30, y+15


def getSelfPos():
    try:
        x, y = pyautogui.monochromeLocateCenterOnScreen(
            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\SelfPos2.png',
            region=(0, 0, 800, 600))
        y = y + 80
        return x, y
    except:
        CreatorRandomV.randomWalk(2)
        return getSelfPos()

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


def reload():
    Input.KeyPress(0x01)
    time.sleep(RandomV.rdp3())
    pyautogui.moveTo(386, 449)
    time.sleep(RandomV.rdp3())
    Input.click()
    time.sleep(RandomV.rd1())
    Input.KeyPress(0x39)
    time.sleep(5)
    Input.KeyPress(0x3C)
    try:
        x,y = pyautogui.locateCenterOnScreen(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\EpicQuest.png',region = (0,0,800,600))
        pyautogui.moveTo(x,y)
        time.sleep(0.5)
        Input.click()
        Input.click()
        print('found epic quest')
    except:
        return
    try:
        x,y = pyautogui.locateCenterOnScreen(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\QuestGuide.png',region = (0,0,800,600))
        pyautogui.moveTo(x,y)
        time.sleep(0.5)
        Input.click()
        Input.click()
        print('click the quest guide')
    except:
        return
    return


def blackMarket():
    if whetherDetect(
            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\BlackMarketLeftDownIdentifier.png',
            (0, 0, 800, 600)) == 1:
        try:
            x, y = getForwardPos()
            if y < 101:  # left down, we set y to be 200 in order to save computability
                Input.KeyPress(0x31)
                time.sleep(RandomV.rdp3())
                pyautogui.moveTo(416, 186)  # center of BM
                Input.click()
                time.sleep(7)
                pyautogui.moveTo(316, 144)
                Input.click()
                time.sleep(6.5)
                Input.KeyPress(0x31)
        except:
            reload()
    elif whetherDetect(
            r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\BlackMarketLeftUpIdentifier.png',
            (0, 0, 800, 300)) == 1:
        try:
            x, y = getForwardPos()
            if y > 470:  # left up
                Input.KeyPress(0x31)
                time.sleep(RandomV.rdp3())
                pyautogui.moveTo(416, 186)  # center of BM
                Input.click()
                time.sleep(6.5)
                Input.KeyPress(0x31)
        except:
            reload()
    elif whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\BlackMarketRightIdentifier.png',
                       (0, 0, 800, 300)) == 1:
        try:  # right, we set y to be smaller than 300 for not confusing with
            Input.PressKey(0x1F)
            time.sleep(2.7)
            Input.ReleaseKey(0x1F)
            x, y = getForwardPos()
            if y < 65:
                Input.KeyPress(0x31)
                pyautogui.moveTo(316, 144)
                Input.click()
                time.sleep(6.5)
                Input.KeyPress(0x31)
        except:
            reload()
    elif whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\BlackMarketSeriaRoom.png',
                       (0, 0, 800, 600)) == 1:
        try:  # Seria Room
            x, y = getForwardPos()
            if y < 95:  # left down, we set y to be 200 in order to save computability
                Input.KeyPress(0x31)
                time.sleep(RandomV.rdp3())
                pyautogui.moveTo(416, 186)  # center of BM
                Input.click()
                time.sleep(4)
                pyautogui.moveTo(316, 144)
                Input.click()
                time.sleep(6.5)
                Input.KeyPress(0x31)
        except:
            reload()
    return


def mount():
    x, y = pyautogui.pLocateCenterOnScreen(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\Forward.png',
                                          region=(0, 0, 800, 600))
    if (y < 120) or (y > 450):
        Input.KeyPress(0x31)
        time.sleep(RandomV.rdp3())
        pyautogui.moveTo(592, 175)
        Input.click()
        time.sleep(7)
        Input.KeyPress(0x31)  # go to the center of Mount
    return


def nearGate():
    Input.KeyPress(0x39)
    print('we are near a gate')
    if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\LeftGate.png',
                     (0, 0, 800, 600)) == 1:
        CreatorGo.goLeft(1.3,0,300)
    elif whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\RightGate.png',
                       (0, 0, 800, 600)) == 1:
        CreatorGo.goRight(1.3,800,300)
    elif whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\DownGate.png',
                       (0, 0, 800, 600)) == 1:
        CreatorGo.goDown(1.3,400,600)
    elif whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\UpGate.png',
                       (0, 0, 800, 600)) == 1:
        try:
            x, y = pyautogui.locateCenterOnScreen(
                r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\UpGate.png', region=(0, 0, 800, 600))
            pyautogui.moveTo(x, y)
            Input.click()
            if 300<x<500:
                if y > 450:
                    CreatorGo.goDown(1.3,x,y)
                else:
                    CreatorGo.goUp(1.3,x,y)
            else:
                if x<400:
                    CreatorGo.goLeft(1.3,x,y)
                else:
                    if y>350:
                        CreatorGo.goRight(1.3,x,y)
                    else:
                        pyautogui.moveTo(x,y)  # a fa li ya ying di mi nei te
                        Input.click()
                        CreatorGo.goRight(1.3,x,y)
        except:
            reload()
    return


def followingForwardVertically():
    try:  # try to locate the avatar twice
        self_x, self_y = getSelfPos()  # y-speed is about 0.7 sec/100 pix
        forward_x, forward_y = getForwardPos()
        print(forward_x,forward_y)
    except:
        CreatorRandomV.randomWalk(1)
        try:
            self_x, self_y = getSelfPos()  # y-speed is about 0.7 sec/100 pix
            forward_x, forward_y = getForwardPos()
        except:
            return
    if abs(self_x - forward_x) < 100 and abs(self_y - forward_y) < 85:
        nearGate()
    else:
        if abs(self_y - forward_y) < 85:
            if forward_y < self_y:
                return
        elif 84 < abs(self_y - forward_y) < 130:
            if forward_y < self_y:
                CreatorGo.goUp(0.35,forward_x,forward_y)
            else:
                CreatorGo.goDown(0.35,forward_x,forward_y)
        else:
            if forward_y < self_y:
                CreatorGo.goUp(0.7,forward_x,forward_y)
            else:
                CreatorGo.goDown(0.7,forward_x,forward_y)
    return


def clickquestNPC():
    x, y = pyautogui.monochromeLocateCenterOnScreen(
        r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\QuestNpc.png', region=(0, 0, 800, 600))
    pyautogui.moveTo(x - 50, y + 150)
    Input.click()


def followingForwardHorizontally():
    try:
        self_x, self_y = getSelfPos()  # y-speed is about 0.7 sec/100 pix
        forward_x, forward_y = getForwardPos()
        print(forward_x,forward_y)
    except:
        CreatorRandomV.randomWalk(1)
        try:
            self_x, self_y = getSelfPos()  # y-speed is about 0.7 sec/100 pix
            forward_x, forward_y = getForwardPos()
        except:
            return
    if abs(self_x - forward_x) < 100 and abs(self_y - forward_y) < 85:
        nearGate()
    else:
        # if abs(self_x - forward_x) < 100:
        #     return
        if 99 < abs(self_x - forward_x) < 170:
            if forward_x < self_x:
                CreatorGo.goLeft(0.7,forward_x,forward_y)
            else:
                CreatorGo.goRight(0.7,forward_x,forward_y)
        else:
            if forward_x < self_x:
                CreatorGo.goLeft(1,forward_x,forward_y)
            else:
                CreatorGo.goRight(1,forward_x,forward_y)
    return


# complete a quest after we have started the dialogue
def completeQuest():
    Input.KeyPress(0x01)
    pyautogui.moveTo(301, 527)
    Input.click()
    try:
        x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown'
                                              r'\QuestCompleted1.png', region=(0, 0, 800, 600))
        pyautogui.moveTo(x, y)
        Input.click()
    except:
        Login.restart()
    return


def chuansongzhen():
    x, y = pyautogui.pLocateCenterOnScreen(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\Forward.png',
                                          region=(0, 0, 800, 600))
    pyautogui.moveTo(x + 200, y + 8)
    time.sleep(RandomV.rdp3())
    Input.click()


def matou():
    x, y = pyautogui.pLocateCenterOnScreen(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\Forward.png',
                                          region=(0, 0, 800, 600))
    pyautogui.moveTo(x, y - 60)
    Input.click()
    time.sleep(RandomV.rd1())
    Input.click()


def Initialization():
    print('Initializing')
    if monochromeWhetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\QuestNpc.png',
                               (0, 0, 800, 600)) == 1:
        clickquestNPC()
        time.sleep(0.5)
        completeQuest()
    if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\MountName.png',
                       (664, 24, 60, 26)) == 1:
        mount()
    if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\BlackMarketName.png',
                       (664, 24, 60, 26)) == 1:
        blackMarket()
    if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\chuansongzhen.png',
                       (0, 0, 600, 600)) == 1:
        chuansongzhen()
    if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\matou.png',
                       (0, 0, 100, 30)) == 1:
        matou()
    if monochromeWhetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\QuestCompleted2.png',(0,0,800,600)) == 1:
        x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\QuestCompleted2.png', region = (0,0,800,600))
        pyautogui.moveTo(x,y)
        Input.click()
    if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\Confirm.png',(0,0,800,600)) == 1:
        x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\Confirm.png', region = (0,0,800,600))
        pyautogui.moveTo(x,y)
        time.sleep(0.5)
        Input.click()
    if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Dungeon\NPKDialogue.png',(0,0,800,600)) == 1:
        Input.KeyPress(0x01)
        time.sleep(0.2)
        Input.KeyPress(0x39)
        time.sleep(0.3)
    if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\CloseWindow.png',(0,0,800,600)) == 1:
        x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\CloseWindow.png', region = (0,0,800,600))
        pyautogui.moveTo(x,y)
        time.sleep(0.5)
        Input.click()


def downtownNavigation():
    Initialization()
    if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\Forward.png',
                     (0, 0, 800, 600)) == 1:
        print('we found forward')
        followingForwardVertically()
        Initialization()
        followingForwardHorizontally()
        downtownNavigation()
    else:  # shadowed or in dungeon or switch
        if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\DungeonIdentifier.png',
                         (484, 570, 100, 30)) == 1:  # in dungeon
            print('dungeon')
            CreatorDungeon.dungeon()
        else:
            time.sleep(3)  # wait for the map switch
            if whetherDetect(r'C:\Users\Administrator\PycharmProjects\DNF_Automation\Downtown\Forward.png',
                             (0, 0, 800, 600)) == 1:
                downtownNavigation()
            else:
                reload()
                downtownNavigation()
