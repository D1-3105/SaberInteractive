from core.BL.Build import Build
from core.configs.config import STORAGES


class TaskStack:
    """
        Interface for list
    """
    _stack: list

    def __init__(self):
        self._stack = []

    def push(self, task):
        if task not in self._stack:  # declare dependency once!
            self._stack.append(task)

    def to_list(self) -> list:
        """
            LIFO
        """
        return self._stack[::-1]

    @property
    def length(self) -> int:
        return len(self._stack)


class TraversalBuild:

    def __init__(self, build: Build):
        self.build = build

    def traversal_build_tasks(self) -> list:
        full_task_list = []
        for task in self.build.dependencies:
            current_task_stack = TaskStack()
            self.traversal_task(current_task_stack, task)
            full_task_list.extend(current_task_stack.to_list())
        return full_task_list

    def traversal_task(self, stack: TaskStack, task_name):
        #  dependencies should be in order they've declared
        stack.push(task_name)
        dependencies = list(STORAGES['tasks'].get_dependencies(task_name))[::-1]
        for task in dependencies:
            self.traversal_task(stack, task)
