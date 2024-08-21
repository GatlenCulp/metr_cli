"""
A Python library for code shared between METR Task Standard tasks.
"""

from .types.infrastructure_types import GPUSpec, FileBuildStep, ShellBuildStep, BuildStep, VMSpec
from .types.task_types import TaskFamily, TaskFamilyMethods, validate_task_family
from .pytest.pytest_plugin import pytest_addoption, task_family, task_name, task

__all__ = [
    "GPUSpec",
    "FileBuildStep",
    "ShellBuildStep",
    "BuildStep",
    "VMSpec",
    "TaskFamily",
    "TaskFamilyMethods",
    "validate_task_family",
    "pytest_addoption",
    "task_family",
    "task_name",
    "task",
]