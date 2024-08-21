import click
from pathlib import Path
from ._npm_helper import run_npm_command, PROJECT_ROOT

@click.command()
@click.argument('task_family_directory', type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.argument('task_name', type=str)
@click.argument('test_file_name', type=str)
def test(task_family_directory: Path, task_name: str, test_file_name: str) -> None:
    """Run tests for a task."""
    abs_task_family_dir = Path(task_family_directory).resolve()
    rel_task_family_dir = abs_task_family_dir.relative_to(PROJECT_ROOT)
    cmd = f"test -- {rel_task_family_dir} {task_name} {test_file_name}"
    cwd = Path.cwd()
    run_npm_command(cmd, cwd)

if __name__ == '__main__':
    test()