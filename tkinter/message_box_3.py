from tkinter import *
from tkinter import messagebox
import time
import pyautogui as pg


def leaveteams():
    time.sleep(5)
    pg.moveTo(3570, 615, 2)
    pg.click(3570, 615)
    time.sleep(2)
    pg.moveTo(343, 552, 2)
    pg.moveTo(200, 652, 1)

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

if messagebox.askretrycancel('Question', "do you have brown hair", icon='error') == True:
    print('yes')
    leaveteams()
else:
    print('no')

window.deiconify()
window.destroy()
window.quit()
