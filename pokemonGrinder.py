import keyboard
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

keyboard.wait('-')
while (not keyboard.is_pressed('shift')):
    pyautogui.keyDown('s')
    pyautogui.keyDown('w')
    pyautogui.keyDown('enter')
    pyautogui.keyDown('enter')