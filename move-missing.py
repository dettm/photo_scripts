# recursively scans the given directory and compares it to another to find any missing files

import os
import shutil

def scan_directory(dir, destination_dir):
    """Recursively scans a directory and prints all files."""

    dir_files = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file[len(file)-4:] == '.JPG' or file[len(file)-4:] == '.NEF':
                dir_files += [(file, root)]

    dest_files = []
    for root, dirs, files in os.walk(destination_dir):
        for file in files:
            if file[len(file)-4:] == '.JPG' or file[len(file)-4:] == '.NEF':
                dest_files += [file]
    
    missing_photos = []
    for photo in dir_files:
        if not photo[0] in dest_files:
            missing_photos += [photo]

    for index, photo in enumerate(missing_photos):
        print(str(index+1) + ': ' + os.path.join(photo[1], photo[0]))

    print('There are ' + str(len(missing_photos)) + ' missing photos.')

    missing_filepaths = [os.path.join(photo[1], photo[0]) for photo in missing_photos]

    return missing_filepaths

def move_missing_photos(missing_filepaths, destination):
    """Move the missing photos to the given destination"""

    dest_folder = "missing_photos"
    if not os.path.exists(destination + '/' + dest_folder):
        os.mkdir(destination + '/' + dest_folder)

    for filepath in missing_filepaths:
        shutil.copyfile(filepath, destination + '/' + dest_folder + '/' + filepath[len(filepath)-12:])
    
    print('Moved missing photos to directory: ' + destination + '/' + dest_folder)


dir = "/Volumes/NIKON D810/DCIM/100ND810"
destination = "/Users/dettm/Documents/Photos"
# dir = "/Users/dettm/Documents/Photos"
# destination = "/Volumes/Primary"


missing = scan_directory(dir, destination)
# move_missing_photos(missing, destination)