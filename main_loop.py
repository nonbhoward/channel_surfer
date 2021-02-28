from cs_hardware_emulation.television import Television
from cs_media_library.vcr import VCR


def main_loop():
    tv, vcr = Television(), VCR()
    tv.channels = vcr.fetch_channel_data()
    while True:
        tv.play_time_of_day_channel()
        exit()


main_loop()
