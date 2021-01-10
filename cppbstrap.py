import os.path
import argparse

from workspacelocation import WorkspaceLocation


def create_project_workspace(location: WorkspaceLocation):
    os.mkdir(location.get_workspace_path())


def create_dir_structure(workspace: WorkspaceLocation):
    os.mkdir(workspace.get_src_path())
    os.mkdir(workspace.get_unit_test_path())


def create_main_cpp_files(location: WorkspaceLocation):
    create_src_main(location)
    create_test_main(location)


def create_src_main(location: WorkspaceLocation):
    static_content = "#include <iostream> \n\n" \
                     "int main() \n" \
                     "{ \n" \
                     "\tstd::cout << \"Hello, World!\" << std::endl; \n" \
                     "\treturn 0;\n" \
                     "}\n"
    with open(os.path.join(location.get_src_path(), "main.cpp"), 'w') as file:
        file.write(static_content)


def create_test_main(location: WorkspaceLocation):
    static_content = "#include <gtest/gtest.h> \n\n" \
                     "int main(int argc, char **argv)\n" \
                     "{\n" \
                     "\t::testing::InitGoogleTest(&argc, argv);\n" \
                     "\treturn RUN_ALL_TESTS();\n" \
                     "}\n"

    with open(os.path.join(location.get_unit_test_path(), "main.cpp"), 'w') as file:
        file.write(static_content)


def create_workspace_cmakelists(project_name: str, location: WorkspaceLocation):
    static_content = "cmake_minimum_required(VERSION 3.17)\n" \
                     "project(" + project_name + ")\n\n" \
                     "set(CMAKE_CXX_STANDARD 14)\n\n" \
                     "include_directories(src)\n" \
                     "add_subdirectory(src)\n" \
                     "add_subdirectory(test)\n"

    with open(os.path.join(location.get_workspace_path(), "CMakeLists.txt"), 'w') as file:
        file.write(static_content)


def create_src_cmakelists(location: WorkspaceLocation):
    static_content = "cmake_minimum_required(VERSION 3.17) \n" \
                     "set(BINARY ${CMAKE_PROJECT_NAME}) \n" \
                     "file(GLOB_RECURSE SOURCES LIST_DIRECTORIES true *.h *.cpp) \n" \
                     "set(SOURCES ${SOURCES}) \n" \
                     "add_executable(${BINARY}_run ${SOURCES}) \n" \
                     "add_library(${BINARY}_lib STATIC ${SOURCES})\n"

    with open(os.path.join(location.get_src_path(), "CMakeLists.txt"), 'w') as file:
        file.write(static_content)


def create_test_cmakelists(location: WorkspaceLocation):
    static_content = "find_package(GTest REQUIRED) \n" \
                     "set(BINARY ${CMAKE_PROJECT_NAME}_tst) \n" \
                     "file(GLOB_RECURSE TEST_SOURCES LIST_DIRECTORIES false *.h *.cpp) \n" \
                     "set(SOURCES ${TEST_SOURCES}) \n" \
                     "add_executable(${BINARY} ${TEST_SOURCES}) \n" \
                     "target_link_libraries(${BINARY} PUBLIC ${CMAKE_PROJECT_NAME}_lib ${GTEST_BOTH_LIBRARIES})\n"

    with open(os.path.join(location.get_unit_test_path(), "CMakeLists.txt"), 'w') as file:
        file.write(static_content)


def create_cmake_lists(project_name: str, location: WorkspaceLocation):
    create_workspace_cmakelists(project_name, location)
    create_src_cmakelists(location)
    create_test_cmakelists(location)


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
    create_cmake_lists(args.Name, project_workspace)
