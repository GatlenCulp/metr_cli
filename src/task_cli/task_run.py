import click
import docker

@click.command()
@click.argument('task_path', type=click.Path(exists=True))
def run(task_path):
    """Run a METR task."""
    client = docker.from_env()
    
    # Build the Docker image
    image, build_logs = client.images.build(path=task_path, tag="metr-task")
    for log in build_logs:
        if 'stream' in log:
            click.echo(log['stream'].strip())

    # Run the container
    container = client.containers.run(
        "metr-task",
        detach=True,
        remove=True
    )

    # Stream the output
    for line in container.logs(stream=True):
        click.echo(line.strip().decode('utf-8'))

    click.echo("Task completed")