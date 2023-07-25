# https://pypi.org/project/PyAutoGUI/

import random
import time
import pyautogui as pag

pag.FAILSAFE = False

while True:
    x = random.randint(200, 1200)
    y = random.randint(200, 900)
    pag.moveTo(x, y, 0.5)
    time.sleep(10)
    pag.press("esc")
    time.sleep(4)
