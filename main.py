import sys, argparse

def create_project_workspace():
    pass


def create_dir_structure():
    pass


def create_main_cpp_files():
    pass


def create_cmake_lists():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='cppbstrap')
    parser.add_argument('name', help='The name of the project')
    args = parser.parse_args()
    print(args.name)
    #parser.print_help()
    #args = parser.parse_args()


    # create_project_workspace()
    # create_dir_structure()
    # create_main_cpp_files()
    # create_cmake_lists()
