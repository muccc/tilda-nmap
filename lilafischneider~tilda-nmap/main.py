### Author: lilafischneider
### Description: Tool which shows visible EMFCamp WiFi access points on a map. Let the badge connect to WiFi first or it might crash.
### Category: location
### License: MIT
### Appname: tilda-nmap
### Built-in: no

import pyb
import math
import ugfx
import buttons
import time
import network
import wifi

loc = utils = __import__("apps/lilafischneider~tilda-nmap/locations")
bs = utils = __import__("apps/lilafischneider~tilda-nmap/bssids")

MAXDIAMETER = 10

ugfx.init()
buttons.init()
buttons.disable_menu_reset()

showMap = True

ugfx.display_image(0,0,'apps/lilafischneider~tilda-nmap/map.gif')
while showMap:
    try:
        apList = wifi.nic().list_aps()
    except OSError:
        # was not able to get ap list,
        # we will just try again
        continue

    # clear image before adding new data
    ugfx.display_image(0,0,'apps/lilafischneider~tilda-nmap/map.gif')
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
                print(i['rssi'], diameter)
  
                ugfx.circle(displayX, displayY, diameter-1, ugfx.RED)
                ugfx.circle(displayX, displayY, diameter, ugfx.RED)

    for i in range(50):        
        if buttons.is_pressed("BTN_MENU"):
            showMap = False
            break
        time.sleep(.1)

