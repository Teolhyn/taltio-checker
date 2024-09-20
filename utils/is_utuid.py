"""
This tool is used to find and return a university id a given path.
"""


def is_id(directoryname):
    """
    is_id is used to find and return a university id a given path.

    Args:
        path (String): a directory path

    Returns:
        String | None: Returns university id or None if one is not found. FIX
    """
    if (5 < len(directoryname) < 8) \
            and not any(x.isupper() for x in directoryname) \
            and not any(x.isdigit() for x in directoryname) \
            and directoryname.isalpha():
        return True
    return False
