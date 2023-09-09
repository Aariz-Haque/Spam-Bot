
import pyautogui,time,keyboard



time.sleep(3)

with open("lyrics.txt",'r') as f:
    for line in f.readlines():
        for word in line.split():
            pyautogui.typewrite(word)
            pyautogui.press('enter')
            if keyboard.is_pressed('q'):
                break