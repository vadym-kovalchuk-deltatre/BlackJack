# https://pypi.org/project/PyAutoGUI/

import pyautogui as pag
import random
import time

pag.FAILSAFE = False

while True:
    x = random.randint(200, 1200)
    y = random.randint(200, 900)
    pag.moveTo(x, y, 0.5)
    time.sleep(10)
    pag.press("esc")
    time.sleep(4)
