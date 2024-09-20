import os

def get_id_from_path(path):
    directoryname = os.path.basename(os.path.normpath(path))
    if (5 < len(directoryname) < 8) and not any(x.isupper() for x in directoryname) and not any(x.isdigit() for x in directoryname):
        return directoryname