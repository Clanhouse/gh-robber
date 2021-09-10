from github import Github
from sqlalchemy.exc import IntegrityError
import forgery_py
from random import seed, randint, choice
from . import db
from app.models import GithubUserInfo, GithubUserInfoSchema

with open("./app/GH_access_token.txt") as f:
    GH_access_token = f.readlines()


def search_for_repositories():
    repositories = g.search_repositories(
        query="language:flask created:=2021-06-27 stars:>100"
    )
    for repo in repositories:
        print("Repo name:", repo.name, ", Repo owner login:", repo.owner.login)
        user_info = GithubUserInfo(
            id=None,
            username=repo.owner.login,
            language=repo.language,
            date=forgery_py.date.date(),
            stars=repo.stargazers_count,  # !!! stars of repo not user !!!
            number_of_repositories=randint(1, 10),
        )
        db.session.add(user_info)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
