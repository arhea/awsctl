import click
from awsctl.commands import install 

@click.group()
def entrypoint():
    pass

entrypoint.add_command(install.install_group)

if __name__ == '__main__':
    entrypoint()
