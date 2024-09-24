"""
taltio_cleaner is a set of tools used to monitor and lint
Taltio data storage.
"""
import os
from utils import utiltools


def find_empty_directories(root_directory):
    """
    find_empty_directories walks through a complete directory-tree starting from a given path.
    It then returns a list of university id's (folder names) that have empty directories, e.g.
    they are not using the data storage.

    Args:
        root_directory (String): Root directory from which the function starts to walk.

    Returns:
        String: University id that is not using the data storage.
    """
    try:
        groups = os.listdir(root_directory)
    except FileNotFoundError:
        print(
            f"Error: The system cannot find the path specified: '{root_directory}'. Are you sure the given path exists?")
        raise

    directories = {}

    for group in groups:
        group_directories = os.listdir(f"{root_directory}\\{group}")
        group_directories_copy = group_directories.copy()
        for directory in group_directories:
            if not utiltools.is_id(directory):
                group_directories_copy.remove(directory)
        directories.update({group: group_directories_copy})

    list_of_empties = []
    for group, directory_list in directories.items():
        directory_list_copy = directory_list.copy()
        for directory in directory_list:
            if os.listdir(f"{root_directory}\\{group}\\{directory}"):
                directory_list_copy.remove(directory)
        list_of_empties.extend(directory_list_copy)

    return list_of_empties


def find_users(root_directory):
    """
    find_empty_directories walks through a complete directory-tree starting from a given path.
    It then returns a list of university id's (folder names) that have empty directories, e.g.
    they are not using the data storage.

    Args:
        root_directory (String): Root directory from which the function starts to walk.

    Returns:
        String: University id that is not using the data storage.
    """

    groups = os.listdir(root_directory)
    directories = {}

    for group in groups:
        group_directories = os.listdir(f"{root_directory}\\{group}")
        group_directories_copy = group_directories.copy()
        for directory in group_directories:
            if not utiltools.is_id(directory):
                group_directories_copy.remove(directory)
        directories.update({group: group_directories_copy})

    list_of_users = []
    for group, directory_list in directories.items():
        directory_list_copy = directory_list.copy()
        for directory in directory_list:
            if not os.listdir(f"{root_directory}\\{group}\\{directory}"):
                directory_list_copy.remove(directory)
        list_of_users.extend(directory_list_copy)

    return list_of_users


def get_email_list(ids):
    """
    Generate a email list for given IDs.

    Args:
        ids str | list: IDs

    Returns:
        str | list: either singular email or email list.
    """
    return utiltools.emailify(ids)


def format_checker(path):
    """

    Args:
        path (_type_): _description_
    """
    structure_warnings = 0
    whitespace_warnings = 0
    missing_iso8601_warnings = 0
    properly_in_format = 0
    total_checked = 0

    empties = find_empty_directories(
        path)  # No need to check empty ones, so let's store them

    users = find_users(path)

    groups = os.listdir(path)

    for group in groups:
        directories = os.listdir(f"{path}\\{group}")
        for directory in directories:
            total_checked += 1
            if directory in empties:
                continue
            try:
                os.listdir(f"{path}\\{group}\\{directory}")
            except NotADirectoryError:
                print(
                    f"STRUCTURE_WARNING: There's a file '{directory}' in a layer '{path}\\{group}' that should have only directories!")
                # structure_warnings += 1
            else:
                names = os.listdir(f"{path}\\{group}\\{directory}")
                for name in names:
                    if any(x.isspace() for x in name):
                        print(
                            f"WHITESPACE_WARNING: File or directory '{name}' in '{path}\\{group}\\{directory}' uses whitespaces!")
                        whitespace_warnings += 1
                    elif name[:2] != "20":
                        print(
                            f"MISSING_ISO8601_WARNING: File or directory '{name}' in '{path}\\{group}\\{directory}' does not use the ISO8061 format!")
                        missing_iso8601_warnings += 1
                    else:
                        print(
                            f"File or directory '{name}' in '{path}\\{group}\\{directory}' is properly formatted :)"
                        )
                        properly_in_format += 1

    msg = (
        f'######################### \n'
        f'# Format check result: \n'
        f'# Total names checked: {total_checked} \n'
        f'# Structure warnings: {structure_warnings} ({structure_warnings/total_checked*100:.2f}%) \n'
        f'# ISO8601 warnings: {missing_iso8601_warnings} ({missing_iso8601_warnings/total_checked*100:.2f}%) \n'
        f'# Whitespace warnings: {whitespace_warnings} ({whitespace_warnings/total_checked*100:.2f}%) \n'
        f'# Properly in format: {properly_in_format} ({properly_in_format/total_checked*100:.2f}%) \n'
        f'######################### \n'
    )
    print(msg)


def main():
    PATH = "Y:"
    utiltools.dashboard()

    cmd = input(
        "What would you like to do? you can input multiple commands by separating them with commas. \n cmd: ")
    cmd_c = cmd.replace(" ", "")
    cmd_list = cmd_c.split(',')
    for i in cmd_list:
        if i == 'e':
            print(find_empty_directories(PATH))
        elif i == 'E':
            print(get_email_list(find_empty_directories(PATH)))
        elif i == 'u':
            print(find_users(PATH))
        elif i == 'f':
            format_checker(PATH)
        else:
            print(
                f"Given command '{i}' is not a command !")


main()
