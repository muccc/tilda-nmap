### Author: lilafischneider
### Description: tilda nmap
### Category: location
### License: MIT
### Appname: tilda-nmap
### Built-in: yes

import pyb
import math
import ugfx
import buttons
import time

ugfx.init()
buttons.init()
buttons.disable_menu_reset()


showMap = 1
while showMap:
    ugfx.text(10,10,"test",ugfx.BLUE)
    time.sleep(10)


