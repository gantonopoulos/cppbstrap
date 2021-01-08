import os.path
import argparse

from WorkspaceLocation import WorkspaceLocation


def create_project_workspace(location: WorkspaceLocation):
    os.mkdir(location.get_workspace_path())


def create_dir_structure(workspace: WorkspaceLocation):
    os.mkdir(workspace.get_src_path())
    os.mkdir(workspace.get_unit_test_path())


def create_main_cpp_files(location: WorkspaceLocation):
    static_content = "#include <iostream> \n\n" \
                     "int main() \n" \
                     "{ \n" \
                     "\tstd::cout << \"Hello, World!\" << std::endl; \n" \
                     "\treturn 0;\n" \
                     "}\n"

    with open(os.path.join(location.get_src_path(), "main.cpp"), 'w') as file:
        file.write(static_content)


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
    absPath = os.path.abspath(args.Path)
    validate_path(absPath)
    project_workspace = WorkspaceLocation(os.path.join(absPath, args.Name))
    create_project_workspace(project_workspace)
    create_dir_structure(project_workspace)
    create_main_cpp_files(project_workspace)
    # create_cmake_lists()
