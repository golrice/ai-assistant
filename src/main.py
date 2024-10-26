import click

@click.group()
def cli():
    pass

@cli.command()
def welcome():
    click.echo("Welcome to AI Assistant!")

# 翻译功能
@cli.command()
@click.option('--text', '-t', required=False, help='The text to be translated.')
@click.option('--path', '-p', required=False, help='The file path to be translated.')
@click.option('--from-lang', '-f', default='en', help='The language to be translated from.')
@click.option('--to-lang', '-l', default='zh', help='The language to be translated to.')
def translate(text, path, from_lang, to_lang):
    if not text and not path:
        click.echo("Please provide either text or file to be translated.")
        return

    click.echo(f"Translating '{text}' from {from_lang} to {to_lang}...")

cli.add_command(welcome)
cli.add_command(translate)

if __name__ == '__main__':
    cli()