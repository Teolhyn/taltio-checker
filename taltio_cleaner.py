import os
from utils import id_from_path as id

def find_empty_directories(root_directory):

    for directory_path, directories, files in os.walk(root_directory):
        if not directories and not files:
            yield id.get_id_from_path(directory_path)
            

path = r"Y:"

print(list(find_empty_directories(path)))