from . import api
from ..models import User, GithubUser


@api.route("/users/")
def get_users():
    users = [user.email for user in User.query.all()]
    return {"users": users}


@api.route("/github-users/")
def get_github_users():
    github_users = [github_user.username for github_user in GithubUser.query.all()]
    return {"github_users": github_users}
