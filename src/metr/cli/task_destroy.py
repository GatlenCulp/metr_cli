import click
from pathlib import Path
from metr.cli._npm_helper import run_npm_command

@click.command()
@click.argument('task_environment_identifier', type=str)
def destroy(task_environment_identifier: str) -> None:
    """Destroy a task environment."""
    cmd = f"destroy -- {task_environment_identifier}"
    cwd = Path.cwd()
    run_npm_command(cmd, cwd)

if __name__ == '__main__':
    destroy()