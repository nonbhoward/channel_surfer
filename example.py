#Example of how to instantiate and use the tvplayer library
from tvplayer import TVPlayer_local
import time
#Place your shows under channels/example_channel/shows
#Place your ads under channels/example_channel/ads
#Acceptable video types are .mp4, .avi, .mkv currently
channel_list=["example_channel1", "example_channel2"]#names in this list must match your folder names under channels/
player = TVPlayer_local(channel_list)
playlist_file, schedule, seek_info = player.initialize() #Builds the channel schedule and saves the playlist file
player.start() #Opens VLC and begins the stream
time.sleep(30)
player.channel_up() #switch to the next channel
time.sleep(30)
player.channel_down() #switch back to previous channel
time.sleep(30)
player.change_channel(0) #changes to channel index 0
time.sleep(30)
player.stop() #Turn off VLC
