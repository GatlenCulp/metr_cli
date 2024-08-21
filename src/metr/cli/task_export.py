import click
from pathlib import Path
from metr.cli._npm_helper import run_npm_command, PROJECT_ROOT

@click.command()
@click.argument('container_name', type=str)
@click.argument('source_path', type=str)
@click.argument('destination_path', type=click.Path(resolve_path=True))
def export(container_name: str, source_path: str, destination_path: Path) -> None:
    """Copy files from a task environment to your computer."""
    abs_destination_path = Path(destination_path).resolve()
    rel_destination_path = abs_destination_path.relative_to(PROJECT_ROOT)
    cmd = f"export -- {container_name} {source_path} {rel_destination_path}"
    cwd = Path.cwd()
    run_npm_command(cmd, cwd)

if __name__ == '__main__':
    export()