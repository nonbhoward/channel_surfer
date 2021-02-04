from pathlib2 import Path
import os
# TODO hardcoded paths, change?
CHANNELS_DIR = 'cs_channels'
CONFIG_DIR = 'cs_configuration'
NETWORKING_DIR = 'cs_networking'
PATHS_DIR = 'cs_paths'
EXTENSION_FILTER = ['bin', 'sh']


class ProjectPaths:
    def __init__(self, project_dir=Path(os.getcwd())):
        self.project_dir = Path(project_dir)
        self.cs_channels = Path(project_dir, CHANNELS_DIR)
        self.cs_config = Path(project_dir, CONFIG_DIR)
        self.cs_networking = Path(project_dir, NETWORKING_DIR)
        self.cs_paths = Path(project_dir, PATHS_DIR)


class SystemPaths:
    def __init__(self, debug=False):
        self.system_root = get_system_root()
        if debug:
            self.all_media_files = get_all_files_in_(self.system_root)


def get_all_files_in_(path_to_search, extension_filter=True) -> dict:
    """
    1. recursively find all files in path
    2. extracts the file extension from every file encountered
    3. if extension is new, create a dict entry for that extension as a list
    4. if extension is known, append the new files
    :param path_to_search: starting point
    :param extension_filter: exclusively find files with these extensions
    :return: all files sorted by extension
    """
    try:
        all_files_by_extension = dict()
        known_extensions = list()
        for root, dirs, files in os.walk(path_to_search):
            for file in files:
                file_extension = get_file_extension_from_(file)
                if extension_filter:
                    if file_extension not in get_extension_filter():
                        continue
                if file_extension not in known_extensions:
                    known_extensions.append(file_extension)
                    all_files_by_extension[file_extension] = list()
                full_path_to_file = Path(root, file)
                all_files_by_extension[file_extension].append(full_path_to_file)
        return all_files_by_extension
    except Exception as e_err:
        print(e_err)


def get_extension_filter() -> list:
    return EXTENSION_FILTER


def get_file_extension_from_(file_to_parse) -> str:
    """
    1. check if delimiter is in file
    2. if not, return empty string
    3. split file by delimiter, use final element as extension
    :param file_to_parse:
    :return:
    """
    try:
        delimiter = '.'
        if delimiter in file_to_parse:
            extension = str(file_to_parse).split(delimiter)[-1]
            if extension:
                return extension
        return ''
    except Exception as e_err:
        print(e_err)


def get_system_root() -> Path:
    try:
        root = Path(os.getcwd()).root
        return root
    except Exception as e_err:
        print(e_err)
