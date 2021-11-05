from github import Github
from sqlalchemy.exc import IntegrityError
from . import db
from app.models import GithubUserInfo
from datetime import datetime


"""
    To do:
        add file 'GH_access_token.txt' to 'backend/app' with github access token 
        token must be without '' and ""
"""

with open("./app/GH_access_token.txt") as f:
    GH_access_token = f.read().strip()


def search_for_user(username=None):

    g = Github(str(GH_access_token))

    langs = []

    for repo in g.get_user(username).get_repos():

        owner = repo.owner.login
        repository_name = repo.name
        date = datetime.date(repo.created_at)
        stars_count = repo.stargazers_count
        public_repos = g.get_user(repo.owner.login).public_repos
        languages = g.get_repo(f"{owner}/{repository_name}").get_languages()

        langs = list(languages.items())
        langs2 = []

        for technology in langs:

            if technology[1] <= 4000:
                break

            elif technology[1] >= 4000:
                langs2.extend(technology[:1])

        found_user = GithubUserInfo.query.filter_by(
            username=repo.owner.login, repository=repo.name
        ).first()

        if found_user:
            return f"User {username} has been found in database"

        else:

            user_info = GithubUserInfo(
                username=owner,
                repository=repository_name,
                languages=langs2,
                date=date,
                stars=stars_count,  # !!! stars of repo not user !!!
                number_of_repositories=public_repos,
            )

            db.session.add(user_info)

    try:
        db.session.commit()
        return f"user {username} has been successfully saved"

    except IntegrityError:
        db.session.rollback()
        return "something wrong"
