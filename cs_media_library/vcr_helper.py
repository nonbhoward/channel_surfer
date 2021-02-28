from cs_media_library.MEDIA_LIB_CONSTANTS import MEDIA_LIB_PATH_NAME
from cs_media_library.MEDIA_LIB_CONSTANTS import SUPPORTED_FILE_EXTENSIONS
from os import getcwd
from os import walk
from pathlib import Path
import logging
logger = logging.getLogger(__name__)


def get_all_file_paths_in_(media_directory=None) -> list:
    """
    1. append a constructed Path object for every file in the media directory
    :param media_directory: media root
    :return: a list containing Paths
    """
    try:
        all_file_paths_in_media_directory = list()
        for root, dirs, files in walk(media_directory):
            for file in files:
                all_file_paths_in_media_directory.append(Path(root, file).resolve())
        return all_file_paths_in_media_directory
    except Exception as e_err:
        print(e_err.args[0])
        logging.error(e_err.args[0])


def get_file_extension_from_(file_path) -> str:
    """
    1. check if file contains a period, anywhere
    2. if yes, remove the final delimited text, likely an extension
    :param file_path: the path to delimit
    :return: a string that will represent a file extension
    """
    try:
        logger.debug(f'get file extension from \'{file_path}\'')
        file_extension = ''
        file_path_contains_delimiter = True if len(str(file_path).split('.')) > 1 else False
        if file_path_contains_delimiter:
            file_extension = str(file_path).split('.')[-1]
        logging.debug(f'found file extension \'{file_extension}\'')
        return file_extension
    except Exception as e_err:
        print(e_err.args[0])
        logging.error(e_err.args[0])


def get_media_library_path() -> Path:
    """
    1. use this module's location as a basis for finding the defined media root
    :return: the Path object of the media root
    """
    try:
        logging.info(f'getting media library path')
        project_path = Path(getcwd())
        project_parent_path = project_path.parent
        media_library_full_path = Path(project_parent_path, MEDIA_LIB_PATH_NAME)
        logging.info(f'media library full path is \'{media_library_full_path.absolute()}\'')
        return media_library_full_path
    except Exception as e_err:
        print(e_err.args[0])
        logging.error(e_err.args[0])


def get_populated_media_library(media_lib_path) -> dict:
    """
    1. recursively get all files in media root
    2. iterate through all of them, for each..
    3. ..strip the extension
    4. ..check that it is supported
    5. ..add supported files to channel content
    :param media_lib_path: the media root
    :return: dict containing media content
    """
    try:
        logging.info(f'populating media library')
        all_media_file_paths = get_all_file_paths_in_(media_lib_path)
        channel_data = dict()
        for file in all_media_file_paths:
            ext = get_file_extension_from_(file)
            if ext in SUPPORTED_FILE_EXTENSIONS:
                path_to_file = Path(*file.parts[:-1])
                if path_to_file not in channel_data:
                    channel_data[path_to_file] = list()
                channel_data[path_to_file].append(file.parts[-1])
        return channel_data
    except Exception as e_err:
        print(e_err.args[0])
        logging.error(e_err.args[0])


if __name__ == '__main__':
    pass
else:
    logging.debug(f'importing \'{__name__}\'')
