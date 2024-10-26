import click

@click.group()
def cli():
    pass

@cli.command()
def welcome():
    click.echo("Welcome to AI Assistant!")

cli.add_command(welcome)

if __name__ == '__main__':
    cli()