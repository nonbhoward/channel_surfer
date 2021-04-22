from typing import Tuple


class ChannelSection:
    def __init__(self):
        self._info = {
            'title':                    None,
            'start_time_rel':           None,
            'end_time_rel':             None,
            'start_time_abs':           None,
            'end_time_abs':             None,
            'video_file_path':          None,
            'video_length':             None,
            'playlist_index':           None}

    @property
    def end_time_absolute(self):
        return self._info['end_time_absolute']

    @end_time_absolute.setter
    def end_time_absolute(self, value):
        self._info['end_time_absolute'] = value

    @property
    def end_time_relative(self):
        return self._info['end_time_relative']

    @end_time_relative.setter
    def end_time_relative(self, value):
        self._info['end_time_relative'] = value

    @property
    def playlist_index(self):
        return self._info['playlist_index']

    @playlist_index.setter
    def playlist_index(self, value):
        self._info['playlist_index'] = value

    @property
    def start_time_absolute(self):
        return self._info['start_time_absolute']

    @start_time_absolute.setter
    def start_time_absolute(self, value):
        self._info['start_time_absolute'] = value

    @property
    def start_time_relative(self):
        return self._info['start_time_relative']

    @start_time_relative.setter
    def start_time_relative(self, value):
        self._info['start_time_relative'] = value

    @property
    def title(self):
        return self._info['title']

    @title.setter
    def title(self, value):
        self._info['title'] = value

    @property
    def video_file_path(self):
        return self._info['video_file_path']

    @video_file_path.setter
    def video_file_path(self, value):
        self._info['video_file_path'] = value

    @property
    def video_length(self):
        return self._info['video_length']

    @video_length.setter
    def video_length(self, value):
        self._info['video_length'] = value


class Channel:
    def __init__(self):
        self._info = {
            'run_time':                 None,
            'channel_name':             None,
            'channel_section_list':     None}

    @property
    def channel_name(self):
        return self._info['channel_name']

    @channel_name.setter
    def channel_name(self, value):
        self._info['channel_name'] = value

    @property
    def channel_section_list(self):
        return self._info['channel_section_list']

    @channel_section_list.setter
    def channel_section_list(self, value):
        self._info['channel_section_list'] = value

    @property
    def run_time(self):
        return self._info['run_time']

    @run_time.setter
    def run_time(self, value):
        self._info['run_time'] = value


class Schedule:
    def __init__(self,
                 int_key:               int,
                 channel_info:          Channel):
        self._info = {
            int_key:                    channel_info
        }

    @property
    def channels(self):
        return self._info

    @channels.setter
    def channels(self, value: Tuple[int, Channel]):
        value_for_channel_integer, value_for_channel = value
        if isinstance(value_for_channel_integer, int) and isinstance(value_for_channel, Channel):
            self._info[value_for_channel_integer] = value_for_channel
            return
        raise TypeError(f'Schedule.channel should be a Tuple[int, Channel]')
