import click
from .src.abnt_converter import convert_to_abnt

@click.command()
@click.option('--name',prompt='Write the name to be converted', help='Name to be converted to ABNT')

def main(name):
    print(convert_to_abnt(name))

if __name__ == '__main__':
    main()
