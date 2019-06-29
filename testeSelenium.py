import sys
#sys.path.append("c:/users/vitor/appdata/local/programs/python/python37/lib/site-packages")
from pynput.mouse import Button, Controller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd



url = 'https://www.google.com.br/'
chrome_options = Options()
chrome_options.add_argument('--window-size=1200,600')
mouse = Controller()

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)

driver.set_window_position(450,234)
winPos = driver.get_window_position()


time.sleep(5)
mousePos = (1481, 384)
relativePos = {'x': abs(winPos['x']-mousePos[0]), 'y': abs(winPos['y']-mousePos[1])}
mouse._position_set((winPos['x'],winPos['y']))
mouse.move(relativePos['x'],relativePos['y'])
mouse.click(Button.left)
time.sleep(5)
driver.close()


