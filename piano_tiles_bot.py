from pyautogui import *
import pyautogui
import time 
import keyboard
import random
import win32api,win32con
# RBG value of black and my screen coordinates it can vary person to person system to system
#RGB: (  0,   0,   0)
# X:  774 Y:  750 RGB: (  0,   0,   0)
# X:  636 Y:  750 RGB: ( 78,  81, 115)
# X:  517 Y:  750 RGB: ( 80,  85, 116)
# X:  409 Y:  750 RGB: ( 80,  82, 115)



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #this pauses the script for 0.01 second:
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:

    if pyautogui.pixel(652,500)[0]==0:
        click(652,500)
    if pyautogui.pixel(544,500)[0]==0:
        click(544,500)
    if pyautogui.pixel(458,500)[0]==0:
        click(458,500)
    if pyautogui.pixel(320,500)[0]==0:
        click(320,500)

        