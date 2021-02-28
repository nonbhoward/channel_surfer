from os import getcwd  # TODO delete if unused outside of debug
from os import walk
from pathlib import Path


class VCR:
    def __init__(self, media_library_root=Path(getcwd()).parent.parent):
        self.supported_file_extensions = ['avi', 'mp4', 'mkv', 'py']
        self.vhs_tapes = self._get_media_library_from_(media_library_root)

    def build_content(self):
        try:
            pass
        except Exception as e_err:
            print(e_err.args[0])

    @staticmethod
    def _get_all_folders_in_(media_library=None, recursive=False) -> list:
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

    @staticmethod
    def _get_all_file_paths_in_(media_directory=None, recursive=False) -> list:
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

    @staticmethod
    def _get_file_extension_from_(file_path) -> str:
        try:
            # TODO the bug is that this is being given a list of folders..
            file_extension = ''
            file_path_contains_delimiter = True if len(str(file_path).split('.')) > 1 else False
            if file_path_contains_delimiter:
                file_extension = str(file_path).split('.')[-1]
            return file_extension
        except Exception as e_err:
            print(e_err.args[0])

    def _get_media_library_from_(self, media_library: Path) -> dict:
        try:
            media_library_folders = self._get_all_folders_in_(media_library)
            library_size = 0
            media_library_content = dict()
            for media_library_folder in media_library_folders:
                if media_library_content is not None:
                    library_size = len(media_library_content)
                if library_size < 1:
                    media_library_content = {
                        media_library_folder: list()
                    }
                all_file_paths = self._get_all_file_paths_in_(media_library_folder)
                for file_path in all_file_paths:
                    file_extension = self._get_file_extension_from_(file_path)
                    if file_extension is not None and file_extension in self.supported_file_extensions:
                        media_library_content[media_library_folder].append(file_path)
            return media_library_content
        except Exception as e_err:
            print(e_err.args[0])


if __name__ == '__main__':
    vcr = VCR()
