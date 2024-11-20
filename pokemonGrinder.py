import keyboard
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = .5

keyboard.wait('-')
while (not keyboard.is_pressed('shift')):
    pyautogui.keyDown('s')
    pyautogui.keyUp('s')
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')