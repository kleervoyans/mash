import click
from utils import fetch_repo_metadata
from summariser import generate_mash

@click.command()
@click.argument('repo_url')
@click.option('--lang', default='EN', help='Output language: EN, DE, TR')
@click.option('--output', default='MASH.md', help='Path to save the Markdown')
```python
def mash(repo_url, lang, output):
    """CLI entry point for Mash (Repo-2-OnePager)."""
    data = fetch_repo_metadata(repo_url)
    md = generate_mash(data, language=lang)
    with open(output, 'w', encoding='utf-8') as f:
        f.write(md)
    click.echo(f'Mash one-pager saved to {output}')

if __name__ == '__main__':
    mash()