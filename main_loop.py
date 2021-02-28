from cs_hardware_emulation.television import Television
from cs_media_library.vcr import VCR


def main_loop():
    tv, vcr = Television(), VCR()
    while True:
        tv.play_time_of_day_channel()


main_loop()
