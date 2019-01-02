"""Enable CLI."""
import json
import click


@click.command()
@click.option('--package', '-P', help='Package name.')
@click.option('--branch', '-B', default=None, help='Branch.')
def cli(package, branch):
    """CLI for this package."""
    from alpinepkgs.packages import get_package
    print(json.dumps(get_package(package, branch), indent=4, sort_keys=True))


cli()  # pylint: disable=E1120
