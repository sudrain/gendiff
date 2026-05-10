import click

from gen_diff.generate_diff import generate_diff


@click.command()
@click.argument("file1", type=click.Path(exists=True, dir_okay=False))
@click.argument("file2", type=click.Path(exists=True, dir_okay=False))
def main(file1, file2):
    """
    Compares two configuration files and shows a difference.
    """
    diff = generate_diff(file1, file2)
    click.echo(diff)
