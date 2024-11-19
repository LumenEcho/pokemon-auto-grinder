import keyboard
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

keyboard.wait('-')
while (not keyboard.is_pressed('shift')):
    pyautogui.press('s', 1)
    pyautogui.press('w', 1)
    pyautogui.press('enter', 1)
    pyautogui.press('enter', 1)