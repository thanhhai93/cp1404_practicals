import shutil
import os
from string import capwords


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        move_file(filename)


def move_file(filename):
    dot_index = filename.find('.')
    ending = filename[dot_index + 1:] if dot_index != -1 else None
    if ending:
        try:
            os.mkdir(ending)
        except:
            pass

        shutil.move(filename, ending + '/' + filename)


main()