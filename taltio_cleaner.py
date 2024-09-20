"""
taltio_cleaner is a set of tools used to monitor and lint
Taltio data storage.
"""
import os
from utils import is_utuid


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

    groups = os.listdir(root_directory)
    directories = {}

    for group in groups:
        group_directories = os.listdir(f"{root_directory}\\{group}")
        group_directories_copy = group_directories.copy()
        for directory in group_directories:
            if not is_utuid.is_id(directory):
                group_directories_copy.remove(directory)
        directories.update({group: group_directories_copy})

    list_of_empties = []
    for group, directory_list in directories.items():
        directory_list_copy = directory_list.copy()
        for directory in directory_list:
            if os.listdir(f"{root_directory}\\{group}\\{directory}"):
                directory_list_copy.remove(directory)
        list_of_empties.extend(directory_list_copy)

    print(list_of_empties)


PATH = r"Y:"

find_empty_directories(PATH)
