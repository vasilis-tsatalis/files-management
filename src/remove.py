import os
import shutil

import sys
import glob
import json

def clear_directory():
    """
    empty the directory (folder) for all files below
    """
    # Opening JSON file
    config_file = open('config.json')
    metadata = json.load(config_file)

    for i in metadata['clear_directories']:
        path = i['dir_path']

        if os.path.isdir(path) and os.path.islink(path):

            for file_name in os.listdir(path):
                # construct full file path
                file = path + file_name

                if os.path.isfile(file):
                    os.remove(file)
                else:
                    raise ValueError("Path {} is not a file.".format(file))
    
    # Closing file
    config_file.close()



def delete_directory():
    """
    remove the directory (folder) and all contents below
    """
    # Opening JSON file
    config_file = open('config.json')
    metadata = json.load(config_file)

    for i in metadata['remove_directories']:
        path = i['dir_path']
        # check if file or directory exists
        if os.path.isdir(path) and os.path.islink(path):
            shutil.rmtree(path)
        else:
            raise ValueError("Path {} is not a directory.".format(path))
    
    # Closing file
    config_file.close()



def delete_file_pattern():
    """
    remove directory (folder) and all contents below
    """
    # Opening JSON file
    config_file = open('config.json')
    metadata = json.load(config_file)

    for i in metadata['file_patterns']:
        path = i['dir_path']
        pattern = i['pattern']

        # Search files with extension in current directory
        data = path+pattern
        files = glob.glob(data)

        # deleting the files with txt extension
        for file in files:
            if os.path.isfile(file):
                os.remove(file)
            else:
                raise ValueError("Path {} is not a file.".format(file))
        
        # Closing file
        config_file.close()
