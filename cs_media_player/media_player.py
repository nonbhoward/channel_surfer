from telnetlib import Telnet
import subprocess
import os
import random
import time

class VideoPlayer_VLC_local:
    def __init__(self, schedule, ip="localhost", port="1234", playlist_name="playlist"):
        self.port=port
        self.ip=ip
        self.playlist_name=playlist_name
        self.schedule=schedule
        self.playlist=""
        self.vlc_telnet = Telnet()
        self.channels = [chan_index for chan_index in schedule.keys()]
        self.start_time = 0
        self.playlist_index_offset = 4 #VLC is stupid and confuses the playlist indexes
        self.build_playlist()
        self.write_playlist()

    def build_playlist(self):
        '''
        constructs the syntax of the vlc playlist file and updates our schedule dict with
        the resulting indexes
        '''
        playlist="#EXTM3U\n"
        for channel_index,schedule in self.schedule.items():
            for schedule_entry in schedule:
                title = self.schedule["title"]
                playlist_string=f"#EXTINF:-1,{title}\n"
                playlist_string+=f"#EXTVLCOPT:start-time={schedule_entry["start_time"]}\n"
                if not(schedule_entry["stop_time"]=="EOV"):
                    playlist_string+=f"#EXTVLCOPT:stop-time={schedule_entry["stop_time"]}\n"
                playlist_string+=schedule_entry["video"]+"\n"
                playlist+=playlist_string
        self.playlist = playlist

    def write_playlist(self,playlist):
        try:
            with open(f"playlists/{self.playlist_name}.m3u","w") as playlist_file:
                playlist_file.write(playlist)
        except:
            raise Exception("failed to write playlist")

    def vlc_seek(self,seconds):
        self.vlc_telnet.open(self.ip,self.port)
        self.vlc_telnet.write(f"seek {str(int(seconds))}\n\r".encode('utf-8'))
        self.vlc_telnet.close()
        
    def vlc_choose_index(self,index):
        self.vlc_telnet.open(self.ip,self.port)
        self.vlc_telnet.write(f"goto {str(index)}\n\r".encode('utf-8'))
        self.vlc_telnet.close()
        
    def vlc_shutdown(self):
        self.vlc_telnet.open(self.ip,self.port)
        self.vlc_telnet.write("shutdown\n\r".encode('utf-8'))
        self.vlc_telnet.close()

    def vlc_pause(self):
        self.vlc_telnet.open(self.ip,self.port)
        self.vlc_telnet.write("pause\n\r".encode('utf-8'))
        self.vlc_telnet.close()

    def vlc_resume(self):
        self.vlc_telnet.open(self.ip,self.port)
        self.vlc_telnet.write("play\n\r".encode('utf-8'))
        self.vlc_telnet.close()
    
    def play(self):
        try:
            self.vlc_process=os.system(f"vlc --no-fullscreen --no-video-on-top --no-random --no-autoscale -I rc --rc-host {self.ip}:{self.port} playlists/{self.playlist_name}.m3u &")
            self.player_start_time = time.time()
        except Exception as e_err:
            print(e_err.args[0])

    def pause(self):
        self.vlc_pause()

    def resume(self):
        self.vlc_resume()

    def stop(self):
        self.vlc_shutdown()




