import os.path
import argparse


class ProjectWorkspace:
    workspace_path: str
    __SOURCE_DIR: str = 'src'
    __UNIT_TESTS_DIR: str = 'test'

    def __init__(self, project_path: str):
        self.workspace_path = project_path

    def get_unit_test_path(self) -> str:
        return os.path.join(self.workspace_path, self.__UNIT_TESTS_DIR)

    def get_src_path(self) -> str:
        return os.path.join(self.workspace_path, self.__SOURCE_DIR)

    def get_workspace_path(self) -> str:
        return self.workspace_path


def create_project_workspace(workspace_path: str):
    os.mkdir(workspace_path)


def create_dir_structure(workspace: ProjectWorkspace):
    os.mkdir(workspace.get_src_path())
    os.mkdir(workspace.get_unit_test_path())


def create_main_cpp_files(workspace: ProjectWorkspace):
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
    absPath = os.path.abspath(args.Path)
    validate_path(absPath)
    project_workspace = ProjectWorkspace(os.path.join(absPath, args.Name))
    create_project_workspace(project_workspace)
    create_dir_structure(project_workspace)
    # create_main_cpp_files()
    # create_cmake_lists()
