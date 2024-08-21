import click
from ._npm_helper import run_npm_command, PROJECT_ROOT
from pathlib import Path

@click.command()
@click.argument('task_family_directory', type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.argument('task_name', type=str)
def run(task_family_directory: Path, task_name: str) -> None:
    """Run a task environment."""
    abs_task_family_dir = Path(task_family_directory).resolve()
    cmd = f"task -- {abs_task_family_dir} {task_name}"
    cwd = Path.cwd()
    print(cwd)  # Keeping the print statement as it was in the original
    run_npm_command(cmd, cwd)

if __name__ == '__main__':
    run()