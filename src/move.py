import os
import shutil
import json


def move_directory():
    """
    move full directory to an other
    source => target
    """
    # Opening JSON file
    config_file = open('./config.json')
    metadata = json.load(config_file)

    for i in metadata['move_dir']:
        source = i['source']
        target = i['target']

        if (os.path.isdir(source) or os.path.exists(source)) and (os.path.isdir(target) or os.path.exists(target)):

            for file_name in os.listdir(source):
                # construct full file path
                s_file = source + file_name
                t_file = target + file_name
                if os.path.isfile(s_file):
                    shutil.copyfile(s_file, t_file)
                    os.remove(s_file)
                else:
                    raise ValueError("File {} is not valid.".format(s_file))
    
    # Closing file
    config_file.close()