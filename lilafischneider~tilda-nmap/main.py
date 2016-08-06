### Author: lilafischneider
### Description: Tool which shows visible EMFCamp WiFi access points on a map. By lilafischneider
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

#import apps.lilafischneider~tilda-nmap.locations as loc
#import apps.lilafischneider~tilda-nmap.bssids as bs

loc = utils = __import__("apps/lilafischneider~tilda-nmap/locations")
bs = utils = __import__("apps/lilafischneider~tilda-nmap/bssids")

MAXDIAMETER = 10

ugfx.init()
buttons.init()
buttons.disable_menu_reset()

showMap = 1

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

        
    time.sleep(5)



