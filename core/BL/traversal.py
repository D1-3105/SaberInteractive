from core.BL.Build import Build
from core.configs.config import STORAGES


class TaskStack:
    """
        Just interface for list
    """
    _stack: list

    def __init__(self):
        self._stack = []

    def push(self, task):
        if task not in self._stack:
            self._stack.append(task)

    def to_list(self):
        return self._stack[::-1]

    @property
    def length(self):
        return len(self._stack)


class TraversalBuild:

    def __init__(self, build: Build):
        self.build = build

    def traversal_build_tasks(self):
        full_task_list = []
        for task in self.build.dependencies:
            current_task_stack = TaskStack()
            self.traversal_task(current_task_stack, task)
            full_task_list.extend(current_task_stack.to_list())
        return full_task_list

    def traversal_task(self, stack: TaskStack, task_name):
        stack.push(task_name)
        dependencies = STORAGES['tasks'].get_dependencies(task_name)
        for task in dependencies:
            self.traversal_task(stack, task)
