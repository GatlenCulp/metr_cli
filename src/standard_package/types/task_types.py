from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Union, Callable, Any
from enum import Enum

class Task(BaseModel):
    id: Union[int, str]
    answer: Optional[str] = None
    requires_picoctf_website: bool = False
    requires_general_internet_read: bool = False
    info: Optional[Any] = None
    instructions: str

class Permission(str, Enum):
    FULL_INTERNET = "full_internet"
    # Add other permissions as needed

class AuxVMSpec(BaseModel):
    # Define the structure of aux VM spec here
    # This is a placeholder and should be updated based on actual requirements
    vm_type: str
    cpu: int
    memory: int
    disk: int

class TaskFamily(BaseModel):
    standard_version: str = "0.3.0"
    
    @classmethod
    def get_instructions(cls, task: Task) -> str:
        ...

    @classmethod
    def install(cls) -> None:
        ...

    @classmethod
    def get_tasks(cls) -> Dict[str, Task]:
        ...

    @classmethod
    def score(cls, task: Task, submission: str) -> Optional[float]:
        ...

    @classmethod
    def start(cls, task: Task) -> None:
        ...

    @classmethod
    def get_permissions(cls, task: Task) -> List[Permission]:
        ...

    @classmethod
    def get_aux_vm_spec(cls, task: Task) -> Optional[AuxVMSpec]:
        ...

# Custom types for method signatures
GetInstructionsType = Callable[[Task], str]
InstallType = Callable[[], None]
GetTasksType = Callable[[], Dict[str, Task]]
ScoreType = Callable[[Task, str], Optional[float]]
StartType = Callable[[Task], None]
GetPermissionsType = Callable[[Task], List[Permission]]
GetAuxVMSpecType = Callable[[Task], Optional[AuxVMSpec]]

class TaskFamilyMethods(BaseModel):
    get_instructions: GetInstructionsType
    install: InstallType
    get_tasks: GetTasksType
    score: ScoreType
    start: Optional[StartType] = None
    get_permissions: Optional[GetPermissionsType] = None
    get_aux_vm_spec: Optional[GetAuxVMSpecType] = None

# A helper function to validate a TaskFamily class
def validate_task_family(task_family_class: type) -> None:
    TaskFamilyMethods(
        get_instructions=task_family_class.get_instructions,
        install=task_family_class.install,
        get_tasks=task_family_class.get_tasks,
        score=task_family_class.score,
        start=getattr(task_family_class, 'start', None),
        get_permissions=getattr(task_family_class, 'get_permissions', None),
        get_aux_vm_spec=getattr(task_family_class, 'get_aux_vm_spec', None)
    )
    # If this doesn't raise an exception, the TaskFamily class is valid