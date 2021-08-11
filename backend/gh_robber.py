import os

import click
from flask_migrate import Migrate, upgrade

from .app.models_helpers import create_fake_data, 
from .app.models import User, GithubUser, GithubUserInfo, GithubUserInfoSchema
from .app import create_app
from .app import db

app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, GithubUser=GithubUser)


@app.cli.command("deploy")
def deploy_cli():
    """Run deployment tasks."""
    upgrade()


@app.cli.command("create_fake_data")
@click.option(
    "--count", default=10, help="Number of fake data to create for each table."
)
def create_fake_data_cli(count):
    """Create fake data for all models."""
    create_fake_data(count)


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
