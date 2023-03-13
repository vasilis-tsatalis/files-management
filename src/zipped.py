# importing required modules
from zipfile import ZipFile
import json
import os
# using datetime module
import datetime


def zip_directory(filename):
    """
    zip the directory (folder) and all files below
    """
    # Opening JSON file
    config_file = open('./config.json')
    metadata = json.load(config_file)

    for i in metadata['zip_directories']:
        path = i['dir_path']
        
        zipname = filename

        if zipname is '':
            zipname = i['zip_name']
            if zipname is '':
                zipname = datetime.datetime.now()

                fullname = path + zipname

                with ZipFile.ZipFile(fullname, 'w', ZipFile.ZIP_DEFLATED) as zipf:
                    zipdir(path, zipf)
    
    # Closing file
    config_file.close()


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))



def extract_directory(filename):
    """
    zip the directory (folder) and all files below
    """
    # Opening JSON file
    config_file = open('./config.json')
    metadata = json.load(config_file)

    for i in metadata['extract_directories']:

        zipname = filename

        if zipname is '':
            zipname = i['fullname']

        if os.path.isfile(zipname) and os.path.exists(zipname):

            # opening the zip file in READ mode
            with ZipFile(zipname, 'r') as zip:
                # printing all the contents of the zip file
                zip.printdir()
                # extracting all the files
                print('Extracting all the files now...')
                zip.extractall()
                print('Done!')
        else:
            raise ValueError("Zip file {} not exists.".format(zipname))
    
    # Closing file
    config_file.close()
