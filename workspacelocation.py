import os.path


class WorkspaceLocation:
    _workspace_path: str
    __SOURCE_DIR: str = 'src'
    __UNIT_TESTS_DIR: str = 'test'

    def __init__(self, project_path: str):
        self._workspace_path = project_path

    def get_unit_test_path(self) -> str:
        return os.path.join(self._workspace_path, self.__UNIT_TESTS_DIR)

    def get_src_path(self) -> str:
        return os.path.join(self._workspace_path, self.__SOURCE_DIR)

    def get_workspace_path(self) -> str:
        return self._workspace_path
