"""
taltio_cleaner is a set of tools used to monitor and lint
Taltio data storage. 
"""
import os
from utils import id_from_path


def find_empty_directories(root_directory):
    """
    find_empty_directories walks through a complete directory-tree starting from a given path.
    It then returns a list of university id's (folder names) that have empty directories, e.g.
    they are not using the data storage.

    Args:
        root_directory (String): Root directory from which the function starts to walk.

    Yields:
        String: University id that is not using the data storage.
    """

    for directory_path, directories, files in os.walk(root_directory):
        if not directories and not files:
            yield id_from_path.get_id_from_path(directory_path)


PATH = r"Y:"

print(list(find_empty_directories(PATH)))
