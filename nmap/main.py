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
import network
import wifi

import apps.nmap.locations as loc
import apps.nmap.bssids as bs




ugfx.init()
buttons.init()
buttons.disable_menu_reset()

showMap = 1
while showMap:
    apList = wifi.nic().list_aps()
    for i in apList:
        # get the human readable version of the bssid
        bssid = ''
        for idx in range(5):
	    bssid += str(hex(i['bssid'][idx])[2:4])
            bssid += ':'
        bssid += str(hex(i['bssid'][5])[2:4])
        # plot circle on map
        
    ugfx.text(10,10,bssid,ugfx.BLUE)
    time.sleep(10)



