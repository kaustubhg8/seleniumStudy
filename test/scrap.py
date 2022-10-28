import pyautogui

import time



def trial1():
    i=1
    while i<1000:
        pyautogui.press('space')
        time.sleep(10)
        i=i+1
        print(i)

trial1()