from itertools import compress
from typing import Generator

import yaml

from core.BL.Build import Build


class GraphStorage:
    node_names: list[str]
    matrix: list[list[int]]


class TaskStorage(GraphStorage):
    def __init__(self, tasks: list):
        self.node_names = list(self.node_names_generator(tasks))
        self.matrix = self.generate_matrix(tasks, self.node_names)

    @classmethod
    def node_names_generator(cls, tasks) -> Generator:
        for task in tasks:
            yield task['name']

    @classmethod
    def generate_matrix(cls, tasks: list, node_names: list[str]):
        matrix = [[] for _ in tasks]
        for task in tasks:
            task_pos = node_names.index(task['name'])
            for node in node_names:
                matrix[task_pos].append(node in task['dependencies'])
        return matrix

    def get_dependencies(self, task_name):
        t_idx = self.node_names.index(task_name)
        dep = self.matrix[t_idx]
        return compress(self.node_names, dep)


class BuildStorage:
    builds: dict

    def __init__(self, builds: list):
        self.builds = {}
        for build in builds:
            build_instance = Build(**build)
            self.builds[build_instance.name] = build_instance

    def get_build(self, build_name):
        return self.builds.get(build_name)


class StorageFactory:
    storage_map: dict

    def __init__(self, type_name):
        self.type_name = type_name

    def storage_class(self):
        return self.storage_map.get(self.type_name)


class DefaultStorageFactory(StorageFactory):
    storage_map = {
        'builds': BuildStorage,
        'tasks': TaskStorage
    }


def load_storage(path):
    with open(path) as f:
        data: dict = yaml.safe_load(f)
    storage_name = list(data.keys())[0]
    storage_class = DefaultStorageFactory(
        storage_name
    ).storage_class()
    storage = storage_class(**data)
    return storage_name, storage

