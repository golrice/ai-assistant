import click
import ai

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
    if text and path:
        click.echo("Please provide either text or file to be translated, not both.")
        return

    if path:
        with open(path, 'r') as f:
            text = f.read()

    click.echo(text)

# 文档解释
@cli.command()
@click.option('--path', '-p', required=True, help='The file path to be explained.')
def explain(path):
    with open(path, 'r') as f:
        text = f.read()

    result = ai.explain(text)
    click.echo(result)

cli.add_command(welcome)
cli.add_command(translate)

if __name__ == '__main__':
    cli()