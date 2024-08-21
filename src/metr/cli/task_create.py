import click
from cookiecutter.main import cookiecutter

TEMPLATE_URL = "https://github.com/GatlenCulp/metr-task-boilerplate"

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--name', required=True, help='Name of the task')
def create(path: click.Path, name: str):
    """Create a new METR task."""  # Replace with actual template URL
    cookiecutter(
        TEMPLATE_URL,
        extra_context={
            'task_name': name,
            'task_type': type,
        },
        output_dir=path,
        no_input=True
    )
    click.echo(f"Task '{name}' created successfully in {path}")