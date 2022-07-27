import pyautogui as pg
import time

# docs - https://pyautogui.readthedocs.io/en/latest/

# pg.size() # see the position of the current window

# pg.position() # see the location of your mouse cursor

# current hang up location - Point(x=1458, y=799)

# https://time.is/
# https://crontab.guru/

time.sleep(5)


# padejau per puse kairio ekrano
def leaveteams():
    pg.moveTo(457, 900, 4)      # 4 leidzia leciau pelytei vaziuoti
    pg.click(457, 900)
    print("I just left teams")


leaveteams()
