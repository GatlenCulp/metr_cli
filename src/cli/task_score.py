import click
from pathlib import Path
from src.cli._npm_helper import run_npm_command

@click.command()
@click.argument('container_name', type=str)
def score(container_name: str) -> None:
    """Run a task environment's scoring function and see the result."""
    cmd = f"score -- {container_name}"
    cwd = Path.cwd()
    run_npm_command(cmd, cwd)

if __name__ == '__main__':
    score()