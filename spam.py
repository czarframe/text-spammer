import pyautogui as line
from time import sleep
sleep(2)
with open('text.txt','r') as spam:
    for i in spam.readlines():
        line.write(i)
        line.press('enter')
        sleep(0.3)