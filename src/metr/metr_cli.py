import click
import pathlib
import sys
import importlib
from rich.traceback import install

install()

CURRENT_DIR = pathlib.Path(__file__).parent
SRC_DIR = CURRENT_DIR.parent

def import_cli_modules():
    if __name__ == '__main__':
        # When run as script, add parent directory to sys.path
        sys.path.insert(0, str(SRC_DIR))
        module_name = "metr.cli"
    else:
        # When imported as a module
        module_name = ".cli"
    
    cli_module = importlib.import_module(module_name, package="metr")
    
    return (
        cli_module.task_create,
        cli_module.task_run,
        cli_module.task_agent,
        cli_module.task_score,
        cli_module.task_export,
        cli_module.task_test,
        cli_module.task_destroy
    )

task_create, task_run, task_agent, task_score, task_export, task_test, task_destroy = import_cli_modules()

@click.group()
def cli():
    """METR CLI for managing METR tasks."""
    pass

cli.add_command(task_create, name="create")
cli.add_command(task_run, name="run")
cli.add_command(task_agent, name="agent")
cli.add_command(task_score, name="score")
cli.add_command(task_export, name="export")
cli.add_command(task_test, name="test")
cli.add_command(task_destroy, name="destroy")

@click.group(name="task")
def task_group():
    """Commands for managing tasks."""
    pass

task_group.add_command(task_create, name="create")
task_group.add_command(task_run, name="run")
task_group.add_command(task_agent, name="agent")
task_group.add_command(task_score, name="score")
task_group.add_command(task_export, name="export")
task_group.add_command(task_test, name="test")
task_group.add_command(task_destroy, name="destroy")

cli.add_command(task_group)

if __name__ == '__main__':
    cli()