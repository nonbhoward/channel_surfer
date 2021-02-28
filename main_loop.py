from cs_hardware_emulation.television import Television
from cs_media_library.vcr import VCR
import logging
logger = logging.getLogger(__name__)


def main_loop():
    logger.info(f'initializing main loop')
    tv, vcr = Television(), VCR()
    channel_data = vcr.fetch_recorded_media()
    tv.build_programming(channel_data)
    while True:
        logger.info(f'entering main loop')
        tv.play_time_of_day_channel()
        exit()


main_loop()
