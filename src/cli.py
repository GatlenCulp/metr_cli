# Entrypoint for all METR CLI commands

import click
from task_cli import task_create, task_run

@click.group()
def cli():
    """METR CLI for managing METR tasks."""
    pass

cli.add_command(task_create.create, name="create")
cli.add_command(task_run.run, name="run")

@click.group(name="task")
def task_group():
    """Commands for managing tasks."""
    pass

task_group.add_command(task_create.create, name="create")
task_group.add_command(task_run.run, name="run")

cli.add_command(task_group)

if __name__ == '__main__':
    cli()