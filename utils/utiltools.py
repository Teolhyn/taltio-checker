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


def emailify(utuid):
    """
    Makes the utuids utu-emails! :)

    Args:
        id String | list: either singular utuid or a list of utuid's 

    Returns:
        String | list: returns either singular utu-email or a list of utu-emails.
        Returns 'None' if input is not instance of str or list.
    """

    email_list = []
    for i in utuid:
        email_list.append(f"{i}@utu.fi")

    return email_list
