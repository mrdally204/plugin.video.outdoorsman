# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/jennamarbles
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.outdoorsman'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
fanart = local.getAddonInfo('fanart')

channels = ["AddictiveFishing", "TheFishingChannel", "walleye101tv", "InDepthOutdoorsTV", "41Hardcore", "keyesoutdoors", "TAFishing", "InformativeFisherman", "uncutangling"]
#playlists = ["PLXx0W3oJrrPQAn9y-DvjGK0tSyyuj25Al"]

# Entry point
def run():
    plugintools.log("AddictiveFishing.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("AddictiveFishing.main_list "+repr(params))
    
    for channel in channels:
		plugintools.add_item(
		title = channel,
		url = "plugin://plugin.video.youtube/user/"+ channel +"/",
		thumbnail = icon,
		folder = True
		)
#for playlist in playlists:
#		plugintools.add_item(
#		title = playlist,
#		url = "plugin://plugin.video.youtube/playlist/"+ playlist +"/",
#		thumbnail = icon,
#		folder = True
#		)

run()