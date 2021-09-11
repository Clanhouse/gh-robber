import os
from flask_migrate import Migrate, upgrade
from app.models import GithubUserInfo
from app import create_app
from app import db

app = create_app()
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, GithubUserInfo=GithubUserInfo)


@app.cli.command("deploy")
def deploy_cli():
    """Run deployment tasks."""
    upgrade()


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
