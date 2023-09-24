from pyautogui import *
import pyautogui
import time 
import keyboard
import random
import win32api,win32con



time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    pic=pyautogui.screenshot(region=(90,428,758,530))

    width,height=pic.size


    # spot color RGB: (255, 219, 195)

    for x in range(0,width,5):
        for y in range(0,height,5):


            r,g,b=pic.getpixel((x,y))
            if b==195 and r==255 and g==219:
                click(x+90,y+428)
                time.sleep(0.10)
                break
      