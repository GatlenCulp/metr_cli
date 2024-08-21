import click
from pathlib import Path
from metr.cli._npm_helper import run_npm_command, PROJECT_ROOT

@click.command()
@click.argument('container_name', type=str)
@click.argument('agent_path', type=click.Path(exists=True, resolve_path=True))
@click.argument('start_command', type=str)
def agent(container_name: str, agent_path: Path, start_command: str) -> None:
    """Run an agent inside a task environment."""
    abs_agent_path = Path(agent_path).resolve()
    rel_agent_path = abs_agent_path.relative_to(PROJECT_ROOT)
    cmd = f"agent -- {container_name} {rel_agent_path} \"{start_command}\""
    cwd = Path.cwd()
    run_npm_command(cmd, cwd)

if __name__ == '__main__':
    agent()