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

MAXDIAMETER = 10


ugfx.init()
buttons.init()
buttons.disable_menu_reset()

showMap = 1

ugfx.display_image(0,0,'apps/nmap/map.gif')
while showMap:
    try:
        apList = wifi.nic().list_aps()
    except OSError:
        # was not able to get ap list,
        # we will just try again
	continue

    # clear image before adding new data
    ugfx.display_image(0,0,'apps/nmap/map.gif')
    for i in apList:
        # get the human readable version of the bssid
        bssid = ''
        for idx in range(5):
	    bssid += str(hex(i['bssid'][idx])[2:4])
            bssid += ':'
        # plot circle on map
        if bssid in bs.bssids:
            # we might see non-aps, we don't look those up
            location = bs.bssids[bssid]
  	    print(location)
            if location in loc.locations:
                displayX = loc.locations[location][0]
                displayY = loc.locations[location][1]
                diameter = int(-1 * (90./i['rssi']) * MAXDIAMETER)
  
                ugfx.circle(displayX, displayY, diameter-1, ugfx.RED)
                ugfx.circle(displayX, displayY, diameter, ugfx.RED)

        
    time.sleep(5)



