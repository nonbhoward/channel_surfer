from cs_media_library.MEDIA_LIB_CONSTANTS import MEDIA_LIB_PATH_NAME
from os import getcwd
from os import walk
from pathlib import Path

import logging
logger = logging.getLogger(__name__)


def get_all_file_paths_in_(media_directory=None, recursive=False) -> list:
    """
    1. TODO, finish func & finish docstring
    :param media_directory:
    :param recursive:
    :return:
    """
    try:
        all_files_in_media_directory = list()
        for root, dirs, files in walk(media_directory):
            surface_files = list()
            if not recursive:
                for _dir in dirs:
                    surface_files.append(Path(root, _dir).absolute())
            for file in files:
                all_files_in_media_directory.append(Path(root, file).resolve())
        return all_files_in_media_directory
    except Exception as e_err:
        print(e_err.args[0])


def get_all_folders_in_(media_library=None, recursive=False) -> list:
    """
    1. if no media library was supplied, raise exception
    2. begin recursive walk through media library
    3. if not recursive, return first level of directories found
    4. else, recursively dive and build list of all directories as Path
    :param media_library: Path, a location on disk containing media, organized by channel
    :param recursive: bool, recursively search if True
    :return: list of Path objects
    """
    try:
        if media_library is None:
            raise Exception('no media library provided!')
        all_dirs_recursive = list()
        for root, dirs, files in walk(media_library):
            if not recursive:
                surface_dirs = list()
                for _dir in dirs:
                    surface_dirs.append(Path(root, _dir).absolute())
                return surface_dirs
            for _dir in dirs:
                all_dirs_recursive.append(Path(root, _dir))
        return all_dirs_recursive
    except Exception as e_err:
        print(e_err.args[0])


def get_file_extension_from_(file_path) -> str:
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


def get_media_library_path() -> Path:
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
    # FIXME entry point for VCR
    :param media_lib_path:
    :return:
    """
    try:
        logging.info(f'populating media library')
        all_media_file_paths = get_all_file_paths_in_(media_lib_path)
        channel_data = dict()
        return channel_data
    except Exception as e_err:
        print(e_err.args[0])
        logging.error(e_err.args[0])


if __name__ == '__main__':
    pass
else:
    logging.debug(f'importing \'{__name__}\'')
