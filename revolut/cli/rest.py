import click
from revolut.rest.login import create_user


def configure(app):
    """Attach new commands to app"""

    @app.cli.command()
    @click.option('--username', '-u', required=True)
    @click.option('--password', '-p', required=True)
    def adduser(username, password):
        """Creates a new admin user"""
        user = create_user(username, password)
        click.echo(f"User {user.id} registered!")