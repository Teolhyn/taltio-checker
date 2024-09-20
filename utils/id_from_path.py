"""
This tool is used to find and return a university id a given path.
"""
import os


def get_id_from_path(path):
    """
    get_id_from_path is used to find and return a university id a given path.

    Args:
        path (String): a directory path

    Returns:
        String | None: Returns university id or None if one is not found.
    """
    directoryname = os.path.basename(os.path.normpath(path))
    if (5 < len(directoryname) < 8) \
            and not any(x.isupper() for x in directoryname) \
            and not any(x.isdigit() for x in directoryname):
        return directoryname
    return
