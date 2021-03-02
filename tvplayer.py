from telnetlib import Telnet
import subprocess
import os
import random
import math
import time

class TVPlayer:
    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.channel_index=0
        self.video_extensions = [".mp4",".avi",".mkv"]
        self.schedule_info={}
        self.seek_info={}
        self.playlist=""
        self.vlc_telnet = Telnet()
        
    def get_video_list(self, foldername):
        file_list= os.listdir(foldername)
        video_list=[]
        for extension in self.video_extensions:
            for file in file_list:
                if file.endswith(extension):
                    video_list.append(foldername+file)
        return video_list
    
    def get_video_lengths(self, video_list):
        results = []
        for video in video_list:
            try:
                length = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                 "format=duration", "-of",
                                 "default=noprint_wrappers=1:nokey=1", video],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT).stdout)
                results.append([video,length])
            except Exception as e:
                raise Exception("Failed to get video length: "+str(video))
        return results
    
    def build_channel_schedule(self,ads,shows):
        show_section_length = (8*60) #8 minutes of show
        min_section_length = (5*60) #Will not creature show sections less than 5 minutes
        ad_section_count = 2 #number of ads per show section
        random.shuffle(shows)
        schedule=[]
        for video_name,video_length in shows:
            num_ad_breaks = math.floor(video_length / show_section_length)
            #prevent super short show sections
            if((video_length%show_section_length)<min_section_length): num_ad_breaks-=1
            #build first show section
            schedule.append({"video":video_name,"video_length":video_length,"start_time":0,"stop_time":show_section_length})
            #build first ad section
            ad_section = random.sample(ads,ad_section_count)
            for ad in ad_section:
                schedule.append({"video":ad[0],"video_length":ad[1],"start_time":0,"stop_time":"EOV"})
            #build interior show sections
            for show_section_index in range(1,num_ad_breaks):
                show_section={"video":video_name,
                              "video_length":video_length,
                              "start_time":(show_section_index*show_section_length),
                              "stop_time":((show_section_index+1)*show_section_length)}
                schedule.append(show_section)
                #add an ad section
                ad_section = random.sample(ads,ad_section_count)
                for ad in ad_section:
                    schedule.append({"video":ad[0],"video_length":ad[1],"start_time":0,"stop_time":"EOV"})
            #build last show section
            schedule.append({"video":video_name,
                        "video_length":video_length,
                          "start_time":(num_ad_breaks*show_section_length),
                          "stop_time":"EOV"})
        return schedule
    
    def build_playlist_and_update_schedule(self,schedule_info):
        playlist_index=0
        playlist_info={}
        playlist="#EXTM3U\n"
        for channel_index,schedule in schedule_info.items():
            for schedule_entry in schedule:
                channel_name = self.channel_list[channel_index]
                schedule_entry["index"]=playlist_index
                playlist_string="#EXTINF:-1,"+channel_name+"\n"
                playlist_string+="#EXTVLCOPT:start-time="+str(schedule_entry["start_time"])+"\n"
                if not(schedule_entry["stop_time"]=="EOV"):
                    playlist_string+="#EXTVLCOPT:stop-time="+str(schedule_entry["stop_time"])+"\n"
                playlist_string+=schedule_entry["video"]+"\n"
                playlist+=playlist_string
                playlist_index+=1
        return playlist
    
    def build_seek_info(self,schedule_info):
        seek_info={}
        for channel_index in schedule_info.keys():
            total_run_time=0
            video_start_time=0
            seek_info[channel_index]={"run_time":0,"time_stamps":[]}
            for video in schedule_info[channel_index]:
                video_timestamp = {}
                video_timestamp["index"]=video["index"]
                video_timestamp["start_time"]=video_start_time
                video_runtime=0
                if video["stop_time"]=="EOV":
                    total_run_time += video["video_length"]-video["start_time"]
                    video_runtime=video["video_length"]-video["start_time"]
                else:
                    total_run_time += video["stop_time"]-video["start_time"]
                    video_runtime = video["stop_time"]-video["start_time"]
                video_timestamp["stop_time"]=video_start_time+video_runtime
                video_timestamp["video_length"]=video["video_length"]
                video_start_time=video_start_time+video_runtime
                seek_info[channel_index]["time_stamps"].append(video_timestamp)
            seek_info[channel_index]["run_time"]=total_run_time           
        return seek_info
    
    def write_playlist(self,playlist):
        try:
            with open("playlist.m3u","w") as playlist_file:
                playlist_file.write(playlist)
        except:
            raise Exception("failed to write playlist")
    
    def vlc_seek(self,seconds):
        self.vlc_telnet.open("localhost",1234)
        self.vlc_telnet.write(str("seek "+str(seconds)+"\n\r").encode('utf-8'))
        self.vlc_telnet.close()
        
    def vlc_choose_index(self,index):
        self.vlc_telnet.open("localhost",1234)
        self.vlc_telnet.write(str("goto "+str(index)+"\n\r").encode('utf-8'))
        self.vlc_telnet.close()
        
    def vlc_shutdown(self):
        self.vlc_telnet.open("localhost",1234)
        self.vlc_telnet.write("shutdown\n\r".encode('utf-8'))
        self.vlc_telnet.close()
    
    def initialize(self):
        schedule_info={}
        for channel_index,channel_name in enumerate(self.channel_list):
            show_filelist = self.get_video_list("channels/"+channel_name+"/shows/")
            show_list = self.get_video_lengths(show_filelist)
            ad_filelist = self.get_video_list("channels/"+channel_name+"/ads/")
            ad_list = self.get_video_lengths(ad_filelist)
            schedule_info[channel_index] = self.build_channel_schedule(ad_list,show_list)
        playlist = self.build_playlist_and_update_schedule(schedule_info)
        self.write_playlist(playlist)
        self.seek_info = self.build_seek_info(schedule_info)
        self.schedule_info = schedule_info
        self.playlist = playlist
        return playlist, schedule_info, self.seek_info
    
    def start(self):
        self.vlc_process=os.system("vlc --no-fullscreen --no-video-on-top --no-random --no-autoscale -I rc --rc-host localhost:1234 playlist.m3u &")
        print("started")
        self.start_time = time.time()
    
    def stop(self):
        self.vlc_shutdown()
    
    def change_channel2(self, channel_index):
        channel_runtime = self.seek_info[channel_index]["run_time"]
        channel_timestamps = self.seek_info[channel_index]["time_stamps"]
        channel_time_offset = (time.time()-self.start_time)%channel_runtime
        target_playlist_index = channel_timestamps[0]["index"]
        target_video_index = 0
        for video_index,video_timestamp in enumerate(channel_timestamps):
            if(video_timestamp["start_time"]>channel_time_offset and
                  video_timestamp["stop_time"]<channel_time_offset):
                target_playlist_index=video_timestamp["index"]
                target_video_index = video_index
        seek_distance = channel_time_offset - channel_timestamps[target_video_index]["start_time"] 
        self.vlc_choose_index(target_playlist_index)
        self.vlc_seek(seek_distance)
        
    def change_channel(self, channel_index):
        channel_time_offset = time.time()-self.start_time
        total_seek_time = 0
        for prev_chan_index in range(0,channel_index):
            total_seek_time += self.seek_info[prev_chan_index]["run_time"]
        total_seek_time += channel_time_offset
        self.vlc_seek(seek_distance)        
        time.sleep(0.5)
        
    def channel_up(self):
        self.channel_index += 1
        if(self.channel_index>=len(self.channel_list)):
            self.channel_index=0
        self.change_channel(self.channel_index)
        
    def channel_down(self):
        if(self.channel_index==0):
            self.channel_index=len(self.channel_list)-1
        else:
            self.channel_index -= 1
        self.change_channel(self.channel_index)