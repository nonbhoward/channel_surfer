from pathlib import Path
from typing import AnyStr
from typing import List


class ChannelSection:
    def __init__(self,
                 title:                 AnyStr,
                 start_time_relative,
                 end_time_relative,
                 start_time_absolute,
                 end_time_absolute,
                 video_file_path:       Path,
                 video_length,
                 playlist_index):
        self._info = {
            'title':                    title,
            'start_time_rel':           start_time_relative,
            'end_time_rel':             end_time_relative,
            'start_time_abs':           start_time_absolute,
            'end_time_abs':             end_time_absolute,
            'video_file_path':          video_file_path,
            'video_length':             video_length,
            'playlist_index':           playlist_index
        }

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        # TODO enforce typing
        self._info = value


class Channel:
    def __init__(self,
                 run_time,
                 channel_name,
                 channel_sections:      List[ChannelSection]):
        self._info = {
            'run_time':                 run_time,
            'channel_name':             channel_name,
            'channel_section_list':     channel_sections
        }

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        # TODO enforce typing
        self._info = value


class Schedule:
    def __init__(self,
                 int_key:               int,
                 channel_info:          Channel):
        self._info = {
            int_key:                    channel_info
        }

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value: tuple):
        int_key, value = value
        if isinstance(int_key, int) and isinstance(value, Channel):
            self._info[int_key] = value
            return
        raise TypeError(f'Schedule.info should be a tuple (int, Channel, )')
