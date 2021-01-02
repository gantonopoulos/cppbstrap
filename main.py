import os.path
import argparse
from typing import Callable


def create_project_workspace():
    pass


def create_dir_structure():
    pass


def create_main_cpp_files():
    pass


def create_cmake_lists():
    pass


def validate_path(path_to_validate: str):
    if not os.path.isdir(path_to_validate):
        raise argparse.ArgumentError('Invalid path!')
    if not os.access(path_to_validate, os.W_OK):
        raise argparse.ArgumentError('Target directory cannot be written. Check access rights!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='cppbstrap')
    parser.add_argument('-p', '--Path', default='.', help='The target directory in which the project\'s workspace '
                                                          'directory will be placed')
    parser.add_argument('Name', help='The name of the project')
    args = parser.parse_args()
    print('Name:' + args.Name)
    print('Path :' + os.path.abspath(args.Path))
    validate_path(os.path.abspath(args.Path))



    # create_project_workspace()
    # create_dir_structure()
    # create_main_cpp_files()
    # create_cmake_lists()
