from cs_hardware_emulation.television import Television
from cs_media_library.vcr import VCR


def main_loop():
    tv, vcr = Television(), VCR()
    tv.play_time_of_day_channel()
    while True:
        tv.wait_for_event()


main_loop()
