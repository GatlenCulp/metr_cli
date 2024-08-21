import click
import sys
import pathlib
from rich.traceback import install
install()

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
WORKBENCH_DIR = PROJECT_ROOT / "src" / "workbench"
sys.path.append(str(PROJECT_ROOT))

from src.cli import task_create, task_run, task_agent, task_score, task_export, task_test, task_destroy


@click.group()
def cli():
    """METR CLI for managing METR tasks."""
    pass

cli.add_command(task_create.create, name="create")
cli.add_command(task_run.run, name="run")
cli.add_command(task_agent.agent, name="agent")
cli.add_command(task_score.score, name="score")
cli.add_command(task_export.export, name="export")
cli.add_command(task_test.test, name="test")
cli.add_command(task_destroy.destroy, name="destroy")

@click.group(name="task")
def task_group():
    """Commands for managing tasks."""
    pass

task_group.add_command(task_create.create, name="create")
task_group.add_command(task_run.run, name="run")
task_group.add_command(task_agent.agent, name="agent")
task_group.add_command(task_score.score, name="score")
task_group.add_command(task_export.export, name="export")
task_group.add_command(task_test.test, name="test")
task_group.add_command(task_destroy.destroy, name="destroy")

cli.add_command(task_group)

if __name__ == '__main__':
    # print(pathlib.Path.cwd())
    cli()