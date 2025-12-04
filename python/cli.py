from __future__ import annotations

import click

import pypalmsens as ps


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    print(f'pypalmsens: {ps.__version__}')
    print(f'libpalmsens: {ps.__sdk_version__}')
    ctx.exit()


@click.group(
    invoke_without_command=False,
)
@click.option(
    '--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True
)
def cli() -> None:
    """CLI tool for PyPalmSens."""
    ...


@click.command()
def discover() -> None:
    """List connected devices."""
    instruments = ps.discover()
    for instrument in instruments:
        print(instrument)


@click.command()
def measure(**kwargs) -> None:
    """Start measurement."""
    print(kwargs)


cli.add_command(discover)
cli.add_command(measure)

if __name__ == '__main__':
    cli()
