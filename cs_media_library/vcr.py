from cs_media_library.vcr_helper import get_media_library_path
from cs_media_library.vcr_helper import get_populated_media_library
import logging
logger = logging.getLogger(__name__)


class VCR:
    def __init__(self):
        logger.debug(f'initializing \'{self.__class__.__name__}\'')
        self.supported_file_extensions = ['avi', 'mp4', 'mkv']
        logger.debug(f'supported file extensions : \'{self.supported_file_extensions}\'')
        med_lib_path = get_media_library_path()
        self.channel_data = get_populated_media_library(med_lib_path)

    def fetch_channel_data(self):
        try:
            logger.info(f'fetching channel data')
            return self.channel_data
        except Exception as e_err:
            print(e_err.args[0])
            logging.error(e_err.args[0])


if __name__ == '__main__':
    vcr = VCR()
    pass
else:
    logging.debug(f'importing \'{__name__}\'')
