import keyboard
import os
on_off = True
def internet_change(x):
    global on_off
    if on_off:
        os.system('ipconfig/release')
    else:
        os.system('ipconfig/renew')
    on_off = not(on_off)
keyboard.on_press_key('f9',internet_change)
keyboard.wait('f8')
